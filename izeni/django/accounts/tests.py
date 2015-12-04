from django.test import TestCase, Client
from .models import EmailUser


class UserTestCase(TestCase):
    def setUp(self):
        self.userInfo = {
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'Firstname',
            'last_name': 'Lastname'
        }
        self.client.post('/api/users/', self.userInfo)
        self.user = EmailUser.objects.get(email=self.userInfo['email'])
        self.client = Client()
        pass

    def test_user_creation(self):
        self.userInfo['email'] = 'test2@example.com'
        response = self.client.post('/api/users/', self.userInfo)
        self.assertEqual(response.status_code, 201)

    def test_user_is_unique(self):
        response = self.client.post('/api/users/', self.userInfo)
        self.assertEqual(response.status_code, 400)

    def test_password_reset(self):
        response = self.client.post(
            '/api/reset-password/{}'.format(self.userInfo['email']))
        print(response.reason_phrase)

    def test_html_email(self):
        pass

    def test_text_email(self):
        pass

    def test_verify_user(self):
        pass
