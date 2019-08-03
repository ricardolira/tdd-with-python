from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.shortcuts import render

from .views import home_page


# Create your tests here.
class HomepageTest(TestCase):

    def test_root_url_reverses_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):

        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('home.html', request=request)

        self.assertTrue(response.content.decode(), expected_html)  # originally assertEqual for django 1

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html',
                                         {'new_item_text': 'A new list itm'})
        self.assertTrue(response.content.decode(), expected_html)  # originally assertIn for django 1
