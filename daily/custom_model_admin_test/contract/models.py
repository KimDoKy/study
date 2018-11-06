from django.db import models

class Contract(models.Model):
    cont_prod = models.ForeignKey('product.Product', related_name='cont_prd', on_delete=models.PROTECT, verbose_name='상품명')
    cont_client = models.ForeignKey('client_info.ClientInfo', related_name='cont_clt', on_delete=models.PROTECT, verbose_name='광고주')
    cont_calc = models.BooleanField(verbose_name='정산여부')
    cont_pay = models.ForeignKey('payment.Payment', on_delete=models.CASCADE, verbose_name='계약금액')

    def __str__(self):
        return f'{self.cont_client}'

    class Meta:
        verbose_name_plural = '계약'
