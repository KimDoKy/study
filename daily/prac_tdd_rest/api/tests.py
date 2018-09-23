from django.test import TestCase
from .models import Post


class ModelTestCase(TestCase):

    def setUp(self):
        self.title = 'post test'
        self.post = Post(title=self.title)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)
