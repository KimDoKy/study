from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class ModelTestCase(TestCase):

    def setUp(self):
        self.title = "Post Model Test Title"
        user = User.objects.create(username='model tester')
        self.post = Post(title=self.title, author=user)

    def test_api_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)
