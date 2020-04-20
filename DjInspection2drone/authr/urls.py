from django.urls import path
from authr import views

urlpatterns = [
    path('', views.auth_list),
]
