from django.db import models
from plan.models import Plan
from company.models import Company


# Create your models here.
class Transaction(models.Model):
    merchant_id = models.CharField(max_length = 150)
    reference_code = models.CharField(max_length=100)
    transaction_state = models.CharField(max_length=100)
    risk = models.FloatField()
    pol_response_code = models.CharField(max_length=300)
    reference_pol = models.CharField(max_length=300)
    signature = models.CharField(max_length=300)
    pol_payment_method = models.CharField(max_length=300)
    pol_payment_method_type = models.IntegerField()
    installments_number = models.IntegerField()
    tx_value = models.IntegerField()
    tx_tax = models.IntegerField()
    processing_date = models.DateField()
    currency = models.CharField(max_length=10)
    cus = models.CharField(max_length=300)
    pse_bank = models.CharField(max_length=300)   
    description = models.CharField(max_length=300)
    iap_response_code = models.CharField(max_length=70)
    iap_payment_method = models.CharField(max_length=300)
    iap_payment_method_type = models.CharField(max_length=300)
    iap_transaction_state = models.CharField(max_length=40)
    message = models.CharField(max_length=300)
    authorization_code = models.CharField(max_length=20)
    pse_cycle = models.IntegerField()
    transaction_id = models.CharField(max_length=40)
    trazability_code = models.CharField(max_length=70)
    plan = models.ForeignKey(Plan, on_delete = models.CASCADE)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)


class Cancel_Or_Refund_Req(models.Model):
    # PayU Request ID for a request in a Transaction.
    request_id = models.CharField(max_length=100)
    # Cancel or Refund or Capture Request
    request_type = models.CharField(max_length=20)
    status = models.CharField(max_length=15)
    message = models.CharField(max_length=100)
    # PayU ID
    mihpayid = models.CharField(max_length=100)
    # Bank Reference Number
    bank_ref_num = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=19, decimal_places=6, default=0)
    error_code = models.CharField(max_length=10)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
