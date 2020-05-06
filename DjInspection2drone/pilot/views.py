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


# Create your views here.
class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    permission_classes = (IsAuthenticated,IsAuthorized,)

    def list(self, request):
        queryset = Pilot.objects.all()
        queryset = Pilot.objects.filter(user_id=request.user.id)  
        qs_json = serializers.serialize('json', queryset)
        return HttpResponse(qs_json, content_type='application/json')


