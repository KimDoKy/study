from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Bucket

class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='test_doky')
        self.name = 'Write code'
        self.bucket = Bucket(name=self.name, owner=user)

    def test_model_can_create_a_bucket(self):
        old_count = Bucket.objects.count()
        self.bucket.save()
        new_count = Bucket.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='test_api_doky')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.bucket_data = {'name': 'view test code', 'owner': user.id}
        self.response = self.client.post(
                reverse('create'),
                self.bucket_data,
                format='json')

    def test_api_can_create_a_bucket(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforce(self):
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk': 3}, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_bucket(self):
        bucket = Bucket.objects.get()
        response = self.client.get(
                reverse('detail', kwargs={'pk':bucket.id}),
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucket)

    def test_api_can_update_a_bucket(self):
        bucket = Bucket.objects.get()
        change_data = {'name': 'change test code'}
        res = self.client.put(
                reverse('detail', kwargs={'pk':bucket.id}),
                change_data,
                format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_bucket(self):
        bucket = Bucket.objects.get()
        response = self.client.delete(
                reverse('detail', kwargs={'pk':bucket.id}),
                format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
