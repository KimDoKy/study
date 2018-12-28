from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class ModelTestCase(TestCase):

    def setUp(self):
        self.author = User.objects.create(username='tester')
        self.author.save()
        self.post_title = "Write test code"
        self.post = Post(author=self.author, title=self.post_title)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)
