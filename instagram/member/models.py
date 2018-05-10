from django.db import models, IntegrityError
import random


class MyUser(models.Model):
    username = models.CharField(
            '유저네임',
            max_length=30,
            unique=True
            )
    last_name = models.CharField(
            '성',
            max_length=20
            )
    first_name = models.CharField(
            '이름',
            max_length=20
            )
    nickname =  models.CharField(
            '닉네임',
            max_length=24
            )
    email = models.EmailField('이메일', blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField(
            'self',
            related_name='follower_set',
            symmetrical=False,
            blank=True
            )

    def __str__(self):
        return self.username

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.followong.remove(user)

    @property
    def followers(self):
        return self.follower_set.all()

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname
        self.save()

    @staticmethod
    def create_dummy_user(num):
        last_name_list = ['김', '허', '이', '박']
        first_name_list = ['도경', '준', '지은', '보검']
        nickname_list = ['doky', '줄을 서시오', '아이유', 'ㅇㅈㅇㅇㅈ']
        created_count = 0
        for i in range(num):
            try:
                MyUser.objects.create(
                        username='User{}'.format(i + 1),
                        last_name=random.choice(last_name_list),
                        first_name=random.choice(first_name_list),
                        nickname=random.choice(nickname_list),
                        )
                created_count += 1
            except IntegrityError as e:
                print(e)
        return created_count

    @staticmethod
    def assign_global_variables():
        import sys
        module = sys.modules['__main__']
        users = MyUser.objects.filter(username__startswith='User')
        for index, user in enumerate(users):
            setattr(module, 'u{}'.format(index+1), user)

