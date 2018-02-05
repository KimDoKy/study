from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='media')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail')
