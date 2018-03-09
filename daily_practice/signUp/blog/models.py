from django.db import models
from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
