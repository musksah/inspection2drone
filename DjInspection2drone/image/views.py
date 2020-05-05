from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Image 
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .serializers import ImageSerializer
from .permissions import IsAuthorizedToCreate
from django.http import HttpResponse, JsonResponse
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,IsAuthorizedToCreate,)

    def list(self, request):
        queryset = Image.objects.all()
        qs_json = serializers.serialize('json', queryset)
        return HttpResponse(qs_json, content_type='application/json')

    def create(self, request):
        # data = JSONParser().parse(request)
        file_r = request.FILES['file']
        name_f = request.FILES['file'].name
        company_id_r = request.POST['company_id']
        form = ImageUploadForm(request.POST,request.FILES)
        fs = FileSystemStorage()
        filename = fs.save(name_f, file_r)
        if form.is_valid():
            response = ["ok"]
        else:
            response = form    
        # company = data["company_id"]
        # file = data["file"]
        # image = Image.objects.create()
        # qs_json = ["Respuesta por el método post"]
        qs_json = [name_f, company_id_r]
        return HttpResponse(qs_json, content_type='application/json')        


def create_image(request):
    data = JSONParser().parse(request)
    username_r = data['username']
    password_r = data['pwd']
    email_r = data['email']
    company_id_r = data['company_id']
    if request.method == 'POST':
        user = User.objects.create_user(
            username = username_r,
            password = password_r,
            email = email_r,
            company_id = company_id_r
        )
        user.save()
    response = {'response': 'El usuario ha sido creado con éxito!',
                'session': False, 'data': data}
    return JsonResponse(response, status=200)


class ImageUploadForm(forms.Form):
    """Image upload form."""
    file = forms.ImageField()
    company_id = forms.CharField()
# Create your views here.
