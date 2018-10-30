from django.db import models
from rest_framework.authtoken.models import Token

class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(author=instance.user)
