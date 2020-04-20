
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.


@csrf_exempt
def auth_list(request):
    """
    Método de autenticación por web request
    """
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        response = {'response': 'Esta petición es por el método get'}
        return JsonResponse(response, status = 200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            response = {'response': 'Usuario encontrado','username':username}
            if user.is_authenticated:
                response.update({'session':True})
            else:
                response.update({'session':False})
        else:
            response = {'response': 'El usuario no existe en la base de datos','session':False}
        return JsonResponse(response, status = 200)


# Create your views here.
