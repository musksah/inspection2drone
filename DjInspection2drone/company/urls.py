from django.urls import path
from company import views

urlpatterns = [
    path('/allcompanies', views.listCompanies)
]
