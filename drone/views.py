from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.views import APIView
from .permissions import IsAuthorized
from .models import Drone
from .serializers import DroneSerializer

# Create your views here.
class DronesView(APIView):
  permission_classes = (IsAuthenticated,IsAuthorized,)

  def get(self, request, format=None):
        drones = Drone.objects.all()
        serializer = DroneSerializer(drones, many=True)
        return JsonResponse(serializer.data, safe=False)