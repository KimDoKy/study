from django.db import models

class Product(models.Model):
    prod_name = models.CharField(max_length=50, unique=True, verbose_name='상품명')
    prod_code = models.AutoField(primary_key=True, verbose_name='상품코드')
    prod_act = models.BooleanField(verbose_name='활성화여부')
    prod_memo = models.TextField(blank=True, null=True, verbose_name='상품 메모')

    class Meta:
        verbose_name_plural = '상품'

    def __str__(self):
        return f'{self.prod_name}'
