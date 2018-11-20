from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='닉네임')
    team = models.ForeignKey('users.Team', blank=True, null=True, on_delete=models.PROTECT, verbose_name='부서')

    def __str__(self):
        return self.nick_name


class Team(models.Model):
    team_code = models.AutoField(primary_key=True, verbose_name='부서코드')
    team_name = models.CharField(max_length=10, verbose_name='부서명')
    team_deps = models.ForeignKey('users.Team', on_delete=models.CASCADE, blank=True, null=True, verbose_name='상위부서')

    def __str__(self):
        return self.team_name
