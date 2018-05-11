from django.db import models
from django.urls import reverse
from django.conf import settings

class Coupon(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=7)
    use_1 = models.BooleanField()
    use_date = models.DateTimeField(auto_now=False, blank=True)
    use_2 = models.BooleanField()
    use_2_date = models.DateTimeField(auto_now=False, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coupon:coupon_list')
