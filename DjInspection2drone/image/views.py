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
        # data e inserción de la tabla de imágenes
        file_r = request.FILES['file']
        name_r = request.FILES['file'].name
        weight_r = request.FILES['file'].size
        drone_id_r = request.POST['drone_id']
        inspection_id_r = request.POST['inspection_id']
        type_image_r = "jepg"
        url_r = f'media/{name_r}' 
        image = Image.objects.create(name=name_r,url=url_r,type_image=type_image_r,size=weight_r,weight=0,drone_id=drone_id_r,inspection_id = inspection_id_r)
        image.save()
        # Guarda la imagen en la carpeta de imágenes
        fs = FileSystemStorage()
        filename = fs.save(name_r, file_r)
        response = ["ok"]
        # form = ImageUploadForm(request.POST,request.FILES)
        return HttpResponse(response, content_type='application/json')        


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
