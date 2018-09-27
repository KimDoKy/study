from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post
from rest_framework.test import APIClient
from rest_framework import status

class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='model_tester')
        self.title = 'Model test title'
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
        self.post_data = {'title':'view test title', 'author':user.id}
        self.response = self.client.post(
                reverse('create'),
                self.post_data,
                format='json')

    def test_api_can_create_a_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
