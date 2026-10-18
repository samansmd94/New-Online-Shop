from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class PagesListViewTest(TestCase):

    # def setUp(self):
    #     self.response = self.client.get(reverse('home'))

    def test_home_page_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_url_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
