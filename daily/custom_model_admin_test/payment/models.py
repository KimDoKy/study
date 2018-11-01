from django.db import models

class Payment(models.Model):
    pmt_money = models.CharField(max_length=14)
    pmt_sell = models.IntegerField(blank=True, null=True)
    pmt_tax = models.IntegerField(blank=True, null=True)
    pmt_comp = models.ForeignKey('PaymentComp', on_delete=models.PROTECT)
    pmt_method = models.ForeignKey('PaymentMethod', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.pmt_tax = int(self.pmt_money) / 11
        self.pmt_sell = int(self.pmt_money) - self.pmt_tax
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.pmt_money}'

class PaymentComp(models.Model):
    company = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.company}'


class PaymentMethod(models.Model):
    PAY_METHOD = (
            ('card','카드'),
            ('bank','현금'),
            )
    pmt_mtd = models.CharField(max_length=10, choices=PAY_METHOD)
    pmt_card = models.ForeignKey('PayCard', on_delete=models.PROTECT, blank=True, null=True)
    pmt_bank = models.ForeignKey('PayBank', on_delete=models.PROTECT, blank=True, null=True)
    
    def get_method(self):
        if self.pmt_mtd == 'card':
            return self.pmt_card
        else:
            return self.pmt_bank

    def __str__(self):
        return f'{self.pmt_mtd}'


class PayCard(models.Model):
    card_sell = models.CharField(max_length=14)
    card_comp = models.ForeignKey('CardComp', on_delete=models.PROTECT)
    card_num = models.CharField(max_length=20)
    card_sell_date = models.DateField()
    card_life = models.CharField(max_length=8)
    card_approval_num = models.CharField(max_length=10)
    card_plan = models.IntegerField()
    card_money = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.card_sell}'


class CardComp(models.Model):
    card_company = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.card_company}'

class PayBank(models.Model):
    BANK_SELECT = (
            ()
            )
    bank_money = models.CharField(max_length=14)
    bank_name = models.CharField(max_length=10, choices=BANK_SELECT)
    bank_in_name = models.CharField(max_length=10)
    bank_date = models.DateField()

    def __str__(self):
        return f'{self.bank_name}'


