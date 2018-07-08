from django.db import models
from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

    def __str__(self):
        return self.title
