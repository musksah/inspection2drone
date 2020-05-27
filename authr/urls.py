from django.urls import path
from authr import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers
from .views import PermissionViewSet

urlpatterns = [
    path('users/list/', views.UsersView.as_view()),
    path('user/new/', views.create_user),
    path('user/new-customer/', views.create_customer),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/obtain_permissions/', views.PermissionViewSet),
]

router = routers.SimpleRouter()
router.register('permissions', PermissionViewSet, basename='permission')
urlpatterns += router.urls

