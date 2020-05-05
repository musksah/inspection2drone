from rest_framework import routers

from .views import ImageViewSet

router = routers.SimpleRouter()
router.register('images', ImageViewSet)

urlpatterns = router.urls
