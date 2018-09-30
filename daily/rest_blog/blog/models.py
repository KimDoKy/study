from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30, blank=False)
    author = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
