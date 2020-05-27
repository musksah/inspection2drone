from django.urls import path
from . import views

urlpatterns = [
    path('transaction/go-pay/', views.TransactionView.as_view()),
    path('transaction/store-pay/', views.TransactionViewStore.as_view()),
]

