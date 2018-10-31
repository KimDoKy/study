from django.db import models

class Product(models.Model):
    prod_name = models.CharField(max_length=50, unique=True)
    prod_code = models.AutoField(primary_key=True)
    prod_act = models.BooleanField()
    prod_memo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.prod_name}'
