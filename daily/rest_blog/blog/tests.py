from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post
from .forms import PostForm

class BlogTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='blog_tester')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.post_data = {'title':'blog test', 'author':user.id}
        self.response = self.client.post(
                reverse('create'),
                self.post_data,
                format='json')

    def test_blog_can_get_post_list(self):
        response = self.client.get(
                '', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_can_get_post_detail(self):
        post = Post.objects.get()
        response = self.client.get(
                reverse('post_detail', kwargs={'pk':post.id}),
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_can_post_post_new(self):
        user = User.objects.get()
        create_data = {'title':'create title', 'author':user.id}
        form = PostForm(data=create_data)
        self.assertTrue(form.is_valid())

