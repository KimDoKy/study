from django.db import models

class ClientInfo(models.Model):
    clt_ceo = models.CharField(max_length=10)
    clt_name = models.CharField(max_length=20)
    clt_biz_num = models.CharField(max_length=13)
    clt_cate_1 = models.CharField(max_length=10, blank=True, null=True)
    clt_cate_2 = models.CharField(max_length=10, blank=True, null=True)
    clt_post = models.CharField(max_length=7)
    clt_addr = models.TextField()
    clt_call = models.CharField(max_length=13, blank=True, null=True)
    clt_phone = models.CharField(max_length=13, blank=True, null=True)
    clt_fax = models.CharField(max_length=13, blank=True, null=True)
    clt_email = models.CharField(max_length=30, blank=True, null=True)
    clt_page = models.TextField(blank=True, null=True)
    clt_person = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.clt_name}'
