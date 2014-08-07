from django.db import models
from payzone.client import Transaction


class PayzoneTransaction(models.Model):
    amount = models.IntegerField()
    customer_token = models.CharField(max_length=500)
    merchant_token = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    code = models.IntegerField(max_length=3)
    status = models.CharField(null=True, max_length=50)
    transaction_id = models.CharField(null=True, max_length=30)

    class Meta:
        app_label = "billing"

    def next_url(self):
        return Transaction.get_dopay_url(self.customer_token)

