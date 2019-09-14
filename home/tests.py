from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import dashboard

# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/home')
        self.assertEqual(found.func, dashboard)

    def test_dashboard_returns_correct_html(self):
        request = HttpRequest()
        response = dashboard(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertContains(response,'<a href=\'/user-list\'>')
        self.assertContains(response,'</a')
        self.assertContains(response,'<h3>Manage lists</h3>')
        self.assertContains(response,'<h3>Make a note</h3>')
        self.assertContains(response,'<h3>Create a reminder</h3>')
        self.assertTrue(html.endswith('</html>'))
