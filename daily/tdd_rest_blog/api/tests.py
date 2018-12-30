from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Post

class ModelTestCase(TestCase):

    def setUp(self):
        user = User(username='tester')
        user.save()
        self.post_title = "Test Title"
        self.post = Post(title=self.post_title, author=user)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)
