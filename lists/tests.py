from django.urls import resolve
from django.test import TestCase
from .views import home_page

# Create your tests here.
class HomepageTest(TestCase):

    def test_root_url_reverses_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
