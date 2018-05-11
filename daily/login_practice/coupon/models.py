from django.db import models
from django.urls import reverse
from django.conf import settings

class Coupon(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=7)
    use_date = models.DateTimeField(auto_now=True, blank=True)
    use_date_2nd = models.DateTimeField(auto_now=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coupon:coupon_list')
