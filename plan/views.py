from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from plan.models import Plan 
from rest_framework import viewsets
from .serializers import PlanSerializer
from .permissions import IsAuthorized

# Create your views here.
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated,IsAuthorized,)
    # authentication_classes = [IsAuthenticated]

    # def get_permissions(self):
        
    #     # if self.action == 'create':
    #     #     permission_classes = [IsAdminUser]
    #     if self.action == 'list':
    #         permission_classes = [IsAuthorized]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsAuthorized]
    #     # elif self.action == 'destroy':
    #     #     permission_classes = [IsLoggedInUserOrAdmin]
    #     return [permission() for permission in permission_classes]