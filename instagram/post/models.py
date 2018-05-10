from django.db import models

from member.models import MyUser


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post', blank=True)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        MyUser,
        through='PostLike',
        related_name='like_post_set',
    )

    def __str__(self):
        return 'Post [{}]'.format(self.id)

    def toggle_like(self, user):
        pl_list = PostLike.objects.filter(post=self, user=user)
        # if pl_list.exists():
        #     pl_list.delete()
        # else:
        #     PostLike.objects.create(post=self, user=user)

        return PostLike.objects.create(post=self, user=user) if not pl_list.exists() else pl_list.delete()

    def add_comment(self, user, content):
        return self.comment_set.create(
            user=user,
            content=content
        )

    @property
    def like_count(self):
        return self.like_users.count()

    @property
    def comment_count(self):
        return self.comment_set.count()

class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Post[{}]\'s Comment[{}], author[{}]'.format(
            self.post_id,
            self.id,
            self.author_id,
        )

class PostLike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('user', 'post'),
        )

    def __str__(self):
        return 'Post [{}]\' Like[{}], User[{}]'.format(
            self.post_id,
            self.id,
            self.user_id,
        )