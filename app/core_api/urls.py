#https://swapi.dev/api/people/
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core_api.views import get_character

app_name='core_api'

urlpatterns = [
    path('character/<int:id>', get_character),
]
