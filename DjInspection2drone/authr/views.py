
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.sessions.backends.db import SessionStore
from rest_framework import generics
from rest_framework_jwt.views import refresh_jwt_token
from django.contrib.auth.models import User

# Create your views here.

# class PostsView(generics.ListAPIView):
#   authentication_class = (JSONWebTokenAuthentication,) # Don't forget to add a 'comma' after first element to make it a tuple
#   permission_classes = (IsAuthenticated,)


@csrf_exempt
def auth_list(request):
    """
    Método de autenticación por web request
    """
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        response = {'response': 'Esta petición es por el método get'}
        return JsonResponse(response, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        s = SessionStore()
        s.create()
        deco = s.model().get_decoded()
        # s.delete(session_key='2b1189a188b44ad18c35e113ac6ceead')
        sessioxn = s.exists(session_key='2b1189a188b44ad18c35e113ac6ceead')

        if user is not None:
            response = {'response': 'Usuario encontrado',
                        'username': username, 'decoded': deco}
            if user.is_authenticated:
                response.update({'session': True})
            else:
                response.update({'session': False})
        else:
            response = {
                'response': 'El usuario no existe en la base de datos', 'session': False}
        return JsonResponse(response, status=200)


@csrf_exempt
def create_user(request):
    data = JSONParser().parse(request)
    username_r = data['username']
    password_r = data['pwd']
    email_r = data['email']
    if request.method == 'POST':
        user = User.objects.create_user(
            username = username_r,
            password = password_r,
            email = email_r
        )
        user.save()
    response = {'response': 'El usuario ha sido creado con éxito!',
                'session': False, 'data': data}
    return JsonResponse(response, status=200)


# Create your views here.
