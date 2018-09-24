from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Post(models.Model):
    title = models.CharField(max_length=20, blank=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(author=request.user)
