from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AccountTests(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = get_user_model().objects.create_user(username=self.username, password=self.password)

    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)  # Redirect on successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Stay on the login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_dashboard_access(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')