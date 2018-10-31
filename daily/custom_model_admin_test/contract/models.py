from django.db import models

class Contract(models.Model):
    cont_prod = models.ForeignKey('product.Product', related_name='cont_prd', on_delete=models.PROTECT)
    cont_client = models.ForeignKey('client_info.ClientInfo', related_name='cont_clt', on_delete=models.PROTECT)
    cont_calc = models.BooleanField()
    cont_pay = models.ForeignKey('payment.Payment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cont_client}'
