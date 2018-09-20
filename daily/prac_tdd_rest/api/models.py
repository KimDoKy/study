from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Bucket(models.Model):
    name = models.CharField(max_length=20, blank=True, unique=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_crated = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
