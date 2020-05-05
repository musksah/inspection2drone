from django.urls import path
from authr import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers
from .views import PermissionViewSet

urlpatterns = [
    path('', views.auth_list),
    path('user/new/', views.create_user),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/obtain_permissions/', views.PermissionViewSet),
]

router = routers.SimpleRouter()
router.register('permissions', PermissionViewSet, basename='permission')
urlpatterns += router.urls

