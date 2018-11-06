from django.db import models

class ClientInfo(models.Model):
    clt_ceo = models.CharField(max_length=10, verbose_name='대표자명')
    clt_name = models.CharField(max_length=20, verbose_name='상호명')
    clt_biz_num = models.CharField(max_length=13, verbose_name='사업자번호')
    clt_cate_1 = models.CharField(max_length=10, blank=True, null=True, verbose_name='업태')
    clt_cate_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name='업종')
    clt_post = models.CharField(max_length=7, verbose_name='우편번호')
    clt_addr = models.TextField(verbose_name='주소')
    clt_call = models.CharField(max_length=13, blank=True, null=True, verbose_name='전화번호')
    clt_phone = models.CharField(max_length=13, blank=True, null=True, verbose_name='휴대폰번호')
    clt_fax = models.CharField(max_length=13, blank=True, null=True, verbose_name='팩스번호')
    clt_email = models.CharField(max_length=30, blank=True, null=True, verbose_name='이메일')
    clt_page = models.TextField(blank=True, null=True, verbose_name='홈페이지')
    clt_person = models.CharField(max_length=10, blank=True, null=True, verbose_name='담당자')

    def __str__(self):
        return f'{self.clt_name}'

    class Meta:
        verbose_name_plural = '광고주'
