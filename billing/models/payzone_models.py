from billing.gateway import get_gateway
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

    def update_status(self):
        # Updating transaction status
        payzone_gt = get_gateway('payzone')
        transaction_status = payzone_gt.payzone.transaction.status(
            self.merchant_token
        )
        self.status = transaction_status['status'].lower()
        self.transaction_id = transaction_status['transactionID']
        self.save()

