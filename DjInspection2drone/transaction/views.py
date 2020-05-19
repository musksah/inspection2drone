from django.shortcuts import render
from rest_framework.views import APIView
from .models import Transaction
from django.forms.models import model_to_dict
from DjInspection2drone import settings


class TransactionView(APIView):

    def get(self, request, format=None):
        #get the last transaction
        last_transaction = Transaction.objects.latest('id')
        data_transaction = model_to_dict(user_last,fields=['id'])
        if len(data_transaction) > 0:
            transaction_last = data_transaction
        else:
            reference_code = "P0001"
        serializer = UserSerializer(Trans-action, many=True)
        reference_code = 0
        # Make the signature md5
        api_key = settings.API_KEY_PAYU
        merchant_id = settings.MERCHANT_ID
        reference_code = self.generateReferenceCode()
        str_pay = "4Vj8eK4rloUd272L48hsrarnUA~508029~P0001~20000~COP"
        value = data['value']
        result_p = hashlib.md5(str_pay.encode())
        signature = result_p.hexdigest()
        # Dict of payu data
        data_pay_u = {
            "merchantId":merchant_id,
            "accountId":settings.ACCOUNT_ID,
            "description":settings.DESCRIPTION_P,
            "amount":settings.DESCRIPTION_P,
            "tax":0,
            "taxReturnBase":0,
            "currency":settings.CURRENCY,
            "signature":signature,
            "test":0,
            "buyerEmail":0,
            "responseUrl":settings.RESPONSE_URL,
            "confirmationUrl":settings.CONFIRMATION_URL,
        }
        return JsonResponse(serializer.data, safe=False)
    
    def generateReferenceCode(self, id):
        pass
# Create your views here.
