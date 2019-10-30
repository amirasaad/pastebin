from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from pastebin.users.tests.factories import UserFactory

User = get_user_model()


class ObtainTokenADITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='user1', password='somethinghard2no')
        self.url = '/api/token/'

    def test_token_api(self):
        resp = self.client.post(self.url, {'username': 'user1', 'password': 'somethinghard2no'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn('access', resp.data)


class UsersAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.url = '/api/v1/users/'
        UserFactory.create_batch(5)

    def test_user_can_list_other_users(self):
        self.client.force_login(self.user)
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], User.objects.all().count())

    def test_user_can_signup(self):
        data = {
            'username': 'ragner',
            'email': 'ragner@example.com',
            'password': 'somethinghard2no'
        }
        resp = self.client.post(self.url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username='ragner')
        self.assertEqual(user.email, data['email'])
