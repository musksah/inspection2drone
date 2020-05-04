from rest_framework import routers

from .views import CompanyViewSet

router = routers.SimpleRouter()
router.register('imgs', CompanyViewSet)

urlpatterns = router.urls
