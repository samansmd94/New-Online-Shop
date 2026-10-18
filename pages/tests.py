from django.test import TestCase

# Create your tests here.

class PagesListViewTest(TestCase):
    def test_home_page_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


