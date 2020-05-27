from rest_framework import routers

from .views import CompanyViewSet

router = routers.SimpleRouter()
router.register('companies', CompanyViewSet)

urlpatterns = router.urls
