from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.core import serializers
from rest_framework.views import APIView
from .permissions import IsAuthorized
from .models import Inspection
from .serializers import InspectionSerializer
from django.http import HttpResponse, JsonResponse

# Create your views here.
class InspectionList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (IsAuthenticated, IsAuthorized,)

    def get(self, request, format=None):
        inspections = Inspection.objects.all()
        serializer = InspectionSerializer(inspections, many=True)
        return JsonResponse(serializer.data, safe=False)