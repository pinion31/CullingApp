from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import create_user, login_user
from django.contrib.auth.models import User
# Create your tests here.
class LoginTest(TestCase):
    def test_root_url_resolves_to_login_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login_user)

    def test_elements_in_template(self):
        request = HttpRequest()
        response = login_user(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
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
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertContains(response, '<input type="text" name="username" maxlength="150" autofocus required id="id_username" />' )
        self.assertContains(response, '<input type="email" name="email" required id="id_email" />' )
        self.assertContains(response, '<input type="password" name="password1" required id="id_password1" />' )
        self.assertContains(response, '<input type="password" name="password2" required id="id_password2" />' )
        self.assertIn('Submit', html)
        self.assertTrue(html.endswith('</html>'))
    
    def test_user_creation(self):
        response = self.client.post(
            '/create-user',data={
                'username': 'chris',
                'password1':'random1!',
                'password2':'random1!',
                'email':'chris@gmail.com' })
        self.assertEqual(User.objects.count(), 1)
        first_user = User.objects.first()
        self.assertEqual(first_user.username, 'chris')
        self.assertEqual(first_user.email, 'chris@gmail.com')
        self.assertTrue(len(first_user.password) > 0)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/home')

    def test_invalid_password_user_creation(self):
        response = self.client.post(
            '/create-user',data={
                'username': 'chris',
                'password1':'test',
                'password2':'test',
                'email':'chris@gmail.com' })
        self.assertEqual(User.objects.count(), 0)
    
    def test_mismatch_password_user_creation(self):
        response = self.client.post(
            '/create-user',data={
                'username': 'chris',
                'password1':'test',
                'password2':'testeeed33',
                'email':'chris@gmail.com' })
        self.assertEqual(User.objects.count(), 0)

        



