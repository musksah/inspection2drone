from rest_framework import routers
from image import views
from django.urls import path

urlpatterns = [
    path('image/create/', views.create_image),
    path('image/list-photos/', views.view_list_images),
]

router = routers.SimpleRouter()
router.register('images', views.ImageViewSet)
urlpatterns += router.urls
