from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Post


class ModelTestCase(TestCase):

    def setUp(self):
        self.title = 'post test'
        self.post = Post(title=self.title)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.post_data = {'title':'view test title'}
        self.response = self.client.post(
                reverse('create'),
                self.post_data,
                format='json')

    def test_api_can_create_a_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
