from django.db import models
from datetime import datetime, timedelta
from . import gps

class TestModel(models.Model):
    
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    end_intern = models.DateTimeField(default=datetime.now()+timedelta(days=90))
    photo = models.ImageField(blank=True)
    gps = models.CharField(max_length=20)
