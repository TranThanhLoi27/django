from django.test import SimpleTestCase

# Create your tests here.
class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class PostsPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

class UpdatPageTest(SimpleTestCase):
    def tes_url_exists_at_correct_location(self):
        response = self.client.get('/posts/update')