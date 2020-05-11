from . import views
from django.urls import path

urlpatterns = [
    path('inspection/list/', views.InspectionList.as_view()),
]
