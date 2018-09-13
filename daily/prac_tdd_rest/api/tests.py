from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Bucket


class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='doky')
        self.name = 'Write code'
        self.bucket = Bucket(name=self.name, owner=user)

    def test_model_can_create_a_bucket(self):
        old_count = Bucket.objects.count()
        self.bucket.save()
        new_count = Bucket.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='doky')

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.bucket_data = {'name':'Go To Doky', 'owner':user.id}
        self.response = self.client.post(
                reverse('create'),
                self.bucket_data,
                format='json')

    def test_api_can_create_a_bucket(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        res = new_client.get(
                '/buckets/',
                kwargs={'pk':3},
                format='json')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_bucket(self):
        bucket = Bucket.objects.get(id=1)
        response = self.client.get(
                '/buckets/', kwargs={'pk':bucket.id},
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucket)

    def test_api_can_update_a_bucket(self):
        bucket = Bucket.objects.get()
        change_bucket = {'name':'Something new'}
        res = self.client.put(
                reverse('details', kwargs={'pk':bucket.id}),
                change_bucket, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_bucket(self):
        bucket = Bucket.objects.get()
        response = self.client.delete(
                reverse('details', kwargs={'pk':bucket.id}),
                format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
