from django.test import TestCase
from .models import Bucket


class ModelTestCase(TestCase):

    def setUp(self):
        self.bucket_name = 'Write code'
        self.bucket = Bucket(name=self.bucket_name)

    def test_api_can_create_a_bucket(self):
        old_count = Bucket.objects.count()
        self.bucket.save()
        new_count = Bucket.objects.count()
        self.assertNotEqual(old_count, new_count)
