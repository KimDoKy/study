from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=20, blank=False, unique=True)
    owner = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
