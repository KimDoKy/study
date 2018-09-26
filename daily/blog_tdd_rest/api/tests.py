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

    def test_api_can_a_get_post(self):
        post = Post.objects.get()
        response = self.client.get(
                '/api/', kwargs={'pk':post.id},
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, post)

    def test_api_can_a_updata_post(self):
        post = Post.objects.get()
        change_data = {'title':'update title',
                       'content':'update content'}
        res = self.client.put(
                reverse('details', kwargs={'pk':post.id}),
                    change_data,
                    format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_a_delete_post(self):
        post = Post.objects.get()
        response = self.client.delete(
                reverse('details', kwargs={'pk':post.id}),
                format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
