from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from blog.models import Post


class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='tester')
        self.title = 'model test title'
        self.post = Post(title=self.title, author=user)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='view_tester')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.post_data = {'title':'view test', 'author':user.id}
        self.response = self.client.post(
            reverse('create'),
            self.post_data,
            format='json')

    def test_api_can_create_a_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_post(self):
        post = Post.objects.get()
        response = self.client.get(
            '/api/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, post)
