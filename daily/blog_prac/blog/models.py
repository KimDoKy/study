from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20, blank=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
