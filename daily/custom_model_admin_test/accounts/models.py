from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    team_1 = models.CharField(max_length=50)
    team_2 = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.team_2:
            return f'{self.team_2} - {self.team_1}'
        else:
            return f'{self.team_1}'

class CustomUser(AbstractUser):
    LEVER_CHOICE = (
            ('ceo','대표이사'),
            ('director','이사'),
            ('manager','부장'),
            ('deputy','차장'),
            ('general','실장'),
            ('main', '본부장'),
            ('team',  '팀장'),
            ('mana','과장'),
            ('assi','주임'),
            ('assi_mana','대리'),
            )
    nick_name = models.CharField(max_length=10)
    level = models.CharField(max_length=20, choices=LEVER_CHOICE, blank=True)
    team_in = models.ManyToManyField('Team')
    def __str__(self):
        return self.username
