from django.urls import resolve
from lists.views import home_page
from django.template.loader import render_to_string
from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        
        self.assertTemplateUsed(response, 'lists/home.html')

