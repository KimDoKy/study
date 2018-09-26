from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post


class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='model tester')
        self.title = 'model test title'
        self.post = Post(title=self.title, author=user)

    def test_model_can_create_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='view tester')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.post_data = {'title':'view test title',
                         'author':user.id,
                         'content':'view test code'}
        self.response = self.client.post(
                reverse('create'),
                self.post_data,
                format='json')

    def test_api_can_a_create_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
