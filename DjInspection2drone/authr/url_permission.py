from rest_framework import routers

from .views import PermissionViewSet

router = routers.SimpleRouter()
router.register('permissions', PermissionViewSet)

urlpatterns = router.urls