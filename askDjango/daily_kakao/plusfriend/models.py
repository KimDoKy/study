from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
