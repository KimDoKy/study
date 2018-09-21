from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
