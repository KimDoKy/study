from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Bucket


class ModelTestCase(TestCase):

    def setUp(self):
        self.name = 'Write code'
        self.bucket = Bucket(name=self.name)

    def test_model_can_create_a_bucket(self):
        old_count = Bucket.objects.count()
        self.bucket.save()
        new_count = Bucket.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.bucket_data = {'name':'view test code'}
        self.response = self.client.post(
                reverse('create'),
                self.bucket_data,
                format='json')

    def test_api_can_create_a_bucket(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
