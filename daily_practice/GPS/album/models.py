from django.db import models
from django.conf import settings

class Album(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    photo = models.ImageField()
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
