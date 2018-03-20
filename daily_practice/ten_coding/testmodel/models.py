from django.db import models
from datetime import datetime, timedelta

class TestModel(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    end_intern = models.DateTimeField(default=datetime.now()+timedelta(days=90))
    photo = models.ImageField(blank=True)
    lat = models.CharField(max_length=10, blank=True)
    lng = models.CharField(max_length=10, blank=True)
