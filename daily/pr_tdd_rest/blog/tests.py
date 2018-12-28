from django.test import TestCase
from .models import Post

class ModelTestCase(TestCase):

    def setUp(self):
        self.post_name = "Write test code"
        self.post = Post(name=self.post_name)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.object.count()
        self.assertEqual(old_count, new_count)
