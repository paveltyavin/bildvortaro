from django.test import Client
from django.test import TestCase


class UrlsTestCase(TestCase):
    def test_main_page(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 201)