from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import create_user, login_user
from django.contrib.auth.models import User
# Create your tests here.
class LoginTest(TestCase):
    def test_root_url_resolves_to_login_view(self):
        found = resolve('/login')
        self.assertEqual(found.func, login_user)

    def test_elements_in_template(self):
        request = HttpRequest()
        response = login_user(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertContains(response, '<input name="username" placeholder="Enter Login" />' )
        self.assertContains(response, '<input name="password" placeholder="Enter Password" />' )
        self.assertIn('Login', html)
        self.assertTrue(html.endswith('</html>'))

class CreateUserTest(TestCase):
    def test_root_url_resolves_to_create_view(self):
        found = resolve('/create-user')
        self.assertEqual(found.func, create_user)

    def test_elements_in_template(self):
        request = HttpRequest()
        response = create_user(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertContains(response, '<input name="username" placeholder="Enter Login" />' )
        self.assertContains(response, '<input name="email" placeholder="Enter Email" />' )
        self.assertContains(response, '<input name="password" placeholder="Enter Password" />' )
        self.assertContains(response, '<input name="password2" placeholder="Confirm Password" />' )
        self.assertIn('Submit', html)
        self.assertTrue(html.endswith('</html>'))
    
    def test_user_creation(self):
        response = self.client.post(
            '/create-user',data={'username': 'chris', 'password':'test','email':'chris@gmail.com' })
        self.assertEqual(User.objects.count(), 1)
        first_user = User.objects.first()
        self.assertEqual(first_user.username, 'chris')
        self.assertEqual(first_user.email, 'chris@gmail.com')
        self.assertTrue(len(first_user.password) > 0)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/home')

        



