from django.test import TestCase


class BlogPageTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')

    def test_posts_page_renders(self):
        response = self.client.get('/posts/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Posts')
