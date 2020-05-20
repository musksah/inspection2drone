import datetime, hashlib
from plan.models import Plan
from django.shortcuts import render
from rest_framework.views import APIView
from transaction.models import Transaction
from django.forms.models import model_to_dict
from DjInspection2drone import settings
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


class TransactionView(APIView):

    def get(self, request, format=None):
        plan_id = request.query_params['plan']
        buyer_email = request.user.email
        plan_list = [plan for plan in Plan.objects.filter(id=plan_id).values()]
        amount = plan_list[0]['price']
        now_str = datetime.datetime.now().strftime("%m%d%H%M%S%f")
        #get the last transaction
        try:
            last_transaction = Transaction.objects.latest('id')
            data_transaction = model_to_dict(last_transaction,fields=['id'])
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
            "merchantId":merchant_id,
            "accountId":settings.ACCOUNT_ID,
            "description":settings.DESCRIPTION_P,
            "referenceCode":reference_code,
            "amount":amount,
            "tax":0,
            "taxReturnBase":0,
            "currency":settings.CURRENCY,
            "signature":signature,
            "test":1,
            "buyerEmail":buyer_email,
            "responseUrl":settings.RESPONSE_URL,
            "confirmationUrl":settings.CONFIRMATION_URL,
        }
        return JsonResponse({'data_pay_u':data_pay_u}, safe=False)
    
# Create your views here.
