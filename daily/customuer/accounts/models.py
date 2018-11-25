from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    team_code = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=10, verbose_name='부서이름')
    team_deps = models.ForeignKey('accounts.Team', null=True, blank=True, on_delete=models.CASCADE, verbose_name='상위부서')

    def __str__(self):
        if self.team_deps:
            return f'{self.team_deps} - {self.team_name}'
        else:
            return f'{self.team_name}'


class CustomUser(AbstractUser):
    name = models.CharField(max_length=5, verbose_name='이름')
    team = models.ForeignKey('accounts.Team', on_delete=models.PROTECT, null=True, blank=True, verbose_name='부서')
    
    def __str__(self):
        return f'{self.name}'
