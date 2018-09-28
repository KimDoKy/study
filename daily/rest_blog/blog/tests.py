from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class BlogTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_blog_can_get_post(self):
        response = self.client.get(
                '', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
