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

class TemplatesViewTest(TestCase):

    def test_login_page_view_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_view_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_logout_page_view_url(self):
        response = self.client.post('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

class TemplatesContentViewTest(TestCase):

    def test_home_page_content(self):
        response = self.client.get('/')
        self.assertContains(response, 'Home Page')

    def test_about_page_content(self):
        response = self.client.get('/aboutus/')
        self.assertContains(response, 'About Us')

    def test_signup_page_content(self):
        response = self.client.get('/accounts/signup/')
        self.assertContains(response, 'Sign Up')

    def test_login_page_content(self):
        response = self.client.get('/accounts/login/')
        self.assertContains(response, 'Log In')