from . import views
from django.urls import path

urlpatterns = [
    path('drone/list/', views.DronesView.as_view()),
]

