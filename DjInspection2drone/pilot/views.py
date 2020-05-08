from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Pilot
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .serializers import PilotSerializer
from .permissions import IsAuthorized
from django.http import HttpResponse, JsonResponse
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os import listdir
from os.path import isfile, join
from django.core import serializers
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


class PilotList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (IsAuthenticated, IsAuthorized,)

    def get(self, request, format=None):
        pilots = Pilot.objects.all()
        serializer = PilotSerializer(pilots, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        id=request.user.id
        data = JSONParser().parse(request)
        all_data = data.items()
        for index, value in all_data:
            if index == "name" and value != "":
                Pilot.objects.filter(user_id = id).update(name = value)
            if index == "lastname" and value != "":
                Pilot.objects.filter(user_id = id).update(lastname = value)
            if index == "email" and value != "":
                Pilot.objects.filter(user_id = id).update(email = value)
            if index == "address" and value != "":
                Pilot.objects.filter(user_id = id).update(address = value)
        response = ['ok']
        return HttpResponse(all_data, content_type='application/json')

# Create your views here.
class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    permission_classes = (IsAuthenticated, IsAuthorized,)

    def list(self, request):
        queryset = Pilot.objects.all()
        queryset = Pilot.objects.filter(user_id=request.user.id)
        qs_json = serializers.serialize('json', queryset)
        return HttpResponse(qs_json, content_type='application/json')
    
