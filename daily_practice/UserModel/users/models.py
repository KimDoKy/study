from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse('login')
