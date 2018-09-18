from django.test import TestCase
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
