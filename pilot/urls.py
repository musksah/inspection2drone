from rest_framework import routers
from pilot import views
from django.urls import path

urlpatterns = [
    path('pilot/update/', views.PilotList.as_view()),
]

router = routers.SimpleRouter()
router.register('pilots', views.PilotViewSet)
urlpatterns += router.urls