from django.db import models
from django.contrib.auth.models import AbstractUser

class CompCategory(models.Model):
    cate_name = models.CharField(max_length=50)
    cate_name_2 = models.ForeignKey('CompCategory', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.cate_name_2:
            return f'{self.cate_name_2} - {self.cate_name}'
        else:
            return self.cate_name

class CustomUser(AbstractUser):
    nick_name = models.CharField(max_length=30)
    comp_cate = models.ManyToManyField('CompCategory', blank=True)
