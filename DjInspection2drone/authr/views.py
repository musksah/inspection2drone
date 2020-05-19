
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.sessions.backends.db import SessionStore
from rest_framework import generics
from rest_framework_jwt.views import refresh_jwt_token
# from django.contrib.auth.models import User
from authr.models import User
from company.models import Company
from .serializers import PermissionSerializer, UserSerializer
from django.contrib.auth.models import Permission
from rest_framework.response import Response
from django.core import serializers
from rest_framework.views import APIView
from .permissions import IsAuthorized
# Create your views here.


class UsersView(APIView):
    permission_classes = (IsAuthenticated, IsAuthorized,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


class PermissionViewSet(viewsets.ModelViewSet):
    # queryset = Permission.objects.all()
    # serializer_class = PermissionSerializer
    # serializer_class = PermissionSerializer
    # permission_classes = (IsAuthenticated,)
    # response = {'response': 'Hola mis perros'}
    # return JsonResponse(response, status=200)
    def list(self, request):
        # queryset = Permission.objects.all()
        # serializer = PermissionSerializer(queryset)
        # serialized_q = json.dumps(list(queryset), cls=DjangoJSONEncoder)
        # return JsonResponse(list(request.user), safe=False)
        queryset = Permission.objects.filter(user=request.user)
        qs_json = serializers.serialize('json', queryset)
        return HttpResponse(qs_json, content_type='application/json')
        # return Response(list(queryset),safe=False)
        # return Response({'response':'hola'})


@csrf_exempt
def create_user(request):
    data = JSONParser().parse(request)
    username_r = data['username']
    password_r = data['pwd']
    email_r = data['email']
    company_id_r = data['company_id']
    if request.method == 'POST':
        user = User.objects.create_user(
            username=username_r,
            password=password_r,
            email=email_r,
            company_id=company_id_r
        )
        user.save()
    response = {'response': 'El usuario ha sido creado con éxito!',
                'session': False, 'data': data}
    return JsonResponse(response, status=200)


@csrf_exempt
def create_customer(request):
    data = JSONParser().parse(request)
    data_company = data['company']
    company = Company(
        nit=data_company['nit'],
        name=data_company['name'],
        email=data_company['email'],
        phone_number=data_company['phone_number'],
        address=data_company['address'],
    )
    company.save()
    id_company = company.id
    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        company_id=id_company
    )
    user.save()
    response = {'message': 'El usuario se creó correctamente!','data': data, 'id':id_company}
    return JsonResponse(response, status=200)

