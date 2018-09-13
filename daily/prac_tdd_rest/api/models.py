from django.db import models


class Bucket(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey('auth.User', related_name='buckets', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
