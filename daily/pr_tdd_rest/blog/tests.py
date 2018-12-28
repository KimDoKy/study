from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import Post

class ModelTestCase(TestCase):

    def setUp(self):
        self.author = User.objects.create(username='tester')
        self.author.save()
        self.post_title = "Write test code"
        self.post = Post(author=self.author, title=self.post_title)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.author = User.objects.create(username='tester')
        self.author.save()
        self.post_data = {'title':'test Title', 'author':self.author.id}
        self.response = self.client.post(
                reverse('create'),
                self.post_data,
                format='json')

    def test_api_can_create_a_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
