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
            ('lv1','대표이사'),
            ('lv2','이사'),
            ('lv3','부장'),
            ('lv4','차장'),
            ('lv5','실장'),
            ('lv6', '본부장'),
            ('lv7',  '팀장'),
            ('lv8','과장'),
            ('lv9','주임'),
            ('lv10','대리'),
            )
    nick_name = models.CharField(max_length=10)
    level = models.CharField(max_length=20, choices=LEVER_CHOICE, blank=True)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.PROTECT, related_name='teamname')

    def __str__(self):
        return self.username
