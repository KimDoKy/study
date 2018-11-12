from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.team

