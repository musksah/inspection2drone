import datetime
import hashlib
from plan.models import Plan
from django.shortcuts import render
from rest_framework.views import APIView
from transaction.models import Transaction
from django.forms.models import model_to_dict
from DjInspection2drone import settings
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import json


class TransactionView(APIView):

    def get(self, request, format=None):
        plan_id = request.query_params['plan']
        buyer_email = request.user.email
        plan_list = [plan for plan in Plan.objects.filter(id=plan_id).values()]
        amount = plan_list[0]['price']
        now_str = datetime.datetime.now().strftime("%m%d%H%M%S%f")
        # get the last transaction
        try:
            last_transaction = Transaction.objects.latest('id')
            data_transaction = model_to_dict(last_transaction, fields=['id'])
            reference_code = f"P{last_transaction.id}{now_str}"
        except:
            reference_code = "P1"+now_str
        # Make the signature md5
        api_key = settings.API_KEY_PAYU
        merchant_id = settings.MERCHANT_ID
        currency = settings.CURRENCY
        str_signature = f"{api_key}~{merchant_id}~{reference_code}~{amount}~{currency}"
        result_p = hashlib.md5(str_signature.encode())
        signature = result_p.hexdigest()
        # Dict of payu data
        data_pay_u = {
            "merchantId": merchant_id,
            "accountId": settings.ACCOUNT_ID,
            "description": settings.DESCRIPTION_P,
            "referenceCode": reference_code,
            "amount": amount,
            "tax": 0,
            "taxReturnBase": 0,
            "currency": settings.CURRENCY,
            "signature": signature,
            "test": 1,
            "buyerEmail": buyer_email,
            "responseUrl": settings.RESPONSE_URL,
            "confirmationUrl": settings.CONFIRMATION_URL,
        }
        return JsonResponse({'data_pay_u': data_pay_u}, safe=False)


class TransactionViewStore(APIView):
    def post(self, request, format=None):
        data_response = request.query_params['data_response']
        data_parsed = json.loads(data_response)
        company_id = request.user.company_id
        transaction = Transaction.objects.create(
            merchant_id=data_parsed["merchantId"],
            reference_code=data_parsed["referenceCode"],
            transaction_state=data_parsed["transactionState"],
            risk= int(data_parsed["risk"]) if data_parsed["risk"]!="" else 0,
            pol_response_code=data_parsed["polResponseCode"],
            signature=data_parsed["signature"],
            pol_payment_method=data_parsed["polPaymentMethod"],
            pol_payment_method_type=data_parsed["polPaymentMethodType"],
            installments_number=data_parsed["installmentsNumber"],
            tx_value=int(float(data_parsed["TX_VALUE"])) if data_parsed["TX_VALUE"]!="" else 0,
            tx_tax=int(float(data_parsed["TX_TAX"])) if data_parsed["TX_TAX"]!="" else 0,
            processing_date=data_parsed["processingDate"],
            currency=data_parsed["currency"],
            cus=data_parsed["cus"],
            pse_bank=data_parsed["pseBank"],
            description=data_parsed["description"],
            iap_response_code=data_parsed["lapResponseCode"],
            iap_payment_method=data_parsed["lapPaymentMethod"],
            iap_transaction_state=data_parsed["lapTransactionState"],
            message=data_parsed["message"],
            authorization_code=data_parsed["authorizationCode"],
            pse_cycle=int(float(data_parsed["pseCycle"])) if data_parsed["pseCycle"]!="" else 0,
            transaction_id=data_parsed["transactionId"],
            trazability_code=data_parsed["trazabilityCode"],
            company_id=company_id,
            plan_id=data_parsed["plan_id"],
        )
        return JsonResponse({'response': "Transación insertada"}, safe=False)

# Create your views here.
