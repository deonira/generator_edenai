from django.urls import path
from .views import image_generation_view

urlpatterns = [
    path('', image_generation_view, name='image_generation'),
]