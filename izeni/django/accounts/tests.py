from urllib.parse import urlparse
import requests
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from .models import EmailUser, get_placeholder_url


class AccountsTestCase(StaticLiveServerTestCase):
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

    def test_html_email(self):
        pass

    def test_text_email(self):
        pass

    def test_verify_user(self):
        pass

    def test_placeholder_profile_url(self):
        # get the placeholder profile url, then reconstruct it with the
        # live test server location instead
        path = urlparse(get_placeholder_url()).path
        url = self.live_server_url + path
        # use a real HTTP request to get the image
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)