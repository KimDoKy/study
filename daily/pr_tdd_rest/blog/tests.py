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

    def test_api_can_get_a_post(self):
        post = Post.objects.get()
        response = self.client.get(
                reverse('details', kwargs={'pk': post.id}),
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, post)

    def test_api_can_a_post(self):
        post = Post.objects.get()
        change_data = {'title':'Change title'}
        res = self.client.put(
                reverse('details', kwargs={'pk':post.id}),
                change_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_a_post(self):
        post = Post.objects.get()
        response = self.client.delete(
                reverse('details', kwargs={'pk':post.id}),
                format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
