from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Image 
from rest_framework import viewsets
from .serializers import ImageSerializer
from .permissions import IsAuthorized

# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,IsAuthorized,)

    

# Create your views here.
