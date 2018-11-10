from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from blog.models import Post

class ModelTestCase(TestCase):

    def setUp(self):
        self.title = "Post Model Test Title"
        user = User.objects.create(username='model tester')
        self.post = Post(title=self.title, author=user)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='view tester')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.post_data = {'title':'view test title', 'author':user.id}
        self.response = self.client.post(
                reverse('create'),
                self.post_data,
                format='json')

    def test_api_can_create_a_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_post(self):
        post = Post.objects.get()
        response = self.client.get(
                reverse('detail', kwargs={'pk':post.id}),
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, post)

    def test_api_can_update_a_post(self):
        user = User.objects.get()
        post = Post.objects.get()
        update_data = {'title':'update title', 'author':user.id}
        response = self.client.put(
                reverse('detail', kwargs={'pk':post.id}),
                update_data,
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_post(self):
        post = Post.objects.get()
        response = self.client.delete(
                reverse('detail', kwargs={'pk':post.id}),
                format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)