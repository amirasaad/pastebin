from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


User = get_user_model()


class ObtainTokenADITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='user1', password='somethinghard2no')
        self.url = '/api-token-auth/'

    def test_token_api(self):
        resp = self.client.post(self.url, {'username': 'user1', 'password': 'somethinghard2no'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        token = Token.objects.get(user=self.user)
        self.assertEqual(resp.data['token'], token.key)

