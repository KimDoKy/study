from django.db import models
from django.conf import settings

class Photo(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    photo = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    album = models.ForeignKey('Album', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
