from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Bucketlist


class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='kdk')
        self.name = 'Write code'
        self.bucketlist = Bucketlist(name=self.name, owner=user)

    def test_model_can_create_a_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='Doky')

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.bucket_data = {'name':'go to DK', 'owner':user.id}
        self.response = self.client.post(
                reverse('create'),
                self.bucket_data,
                format='json')

    def test_api_can_create_a_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk':3}, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
                reverse('details', kwargs={'pk':bucketlist.id}),
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_a_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        bucketlist_data = {'name':'Doky'}
        res = self.client.put(
                reverse('details', kwargs={'pk':bucketlist.id}),
                bucketlist_data,
                format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
                reverse('details', kwargs={'pk':bucketlist.id}),
                format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
