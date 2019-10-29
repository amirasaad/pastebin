from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.test import APITestCase

# - Each user can create edit delete any of his pastes.
# - Allow anonymous guests to create pastes as well.
# - Each user can filter pastes by dates.
# - Each user can choose to share this paste with certain users
# - Token-based authentication system.
from pastebin.pastes.tests.factories import PasteFactory
from pastebin.users.tests.factories import UserFactory
from pastebin.pastes.models import Paste


class PastesTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.url = '/api/v1/pastes/'

    def test_user_can_create_paste(self):
        self.client.force_login(self.user)
        code = "print('Hello World')"
        data = {'content': code}
        resp = self.client.post(self.url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Paste.objects.all().count(), 1)
        paste = Paste.objects.get()
        self.assertEqual(paste.content, code)

    def test_user_can_edit_his_paste(self):
        self.client.force_login(self.user)
        paste = Paste.objects.create(owner=self.user, content='text')
        data = {'content': 'print("New Text"'}
        resp = self.client.put(f"{self.url}{paste.pk}/", data)
        paste.refresh_from_db()
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(paste.content, data['content'])

    def test_user_can_not_edit_other_paste(self):
        self.client.force_login(self.user)
        paste = Paste.objects.create(owner=UserFactory(), content='text')
        data = {'content': 'print("New Text"'}
        resp = self.client.put(f"{self.url}{paste.pk}/", data)
        paste.refresh_from_db()
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_his_paste(self):
        self.client.force_login(self.user)
        paste = Paste.objects.create(owner=self.user, content='text')
        resp = self.client.delete(f"{self.url}{paste.pk}/")
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_not_delete_other_paste(self):
        self.client.force_login(self.user)
        paste = Paste.objects.create(owner=UserFactory(), content='text')
        resp = self.client.delete(f"{self.url}{paste.pk}/")
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_can_create_paste(self):
        code = "print('Hello World')"
        data = {'content': code}
        resp = self.client.post(self.url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Paste.objects.all().count(), 1)
        paste = Paste.objects.get()
        self.assertEqual(paste.content, code)

    def test_user_can_filter_pastes_by_dates(self):
        self.client.force_login(self.user)
        now = datetime.now()
        pastes = PasteFactory.create_batch(5)
        url = f'{self.url}?created__gt={now.strftime("%Y-%m-%d")}'
        print(url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 5)
