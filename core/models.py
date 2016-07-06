from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=50)
    credit_card = models.BigIntegerField()
    pin_code = models.IntegerField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_detail = models.CharField(max_length=128)
    date = models.DateTimeField
    amount = models.DecimalField(max_digits=10, decimal_places=2)
