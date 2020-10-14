#https://swapi.dev/api/people/
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core_api.views import charTest, get_char_by_id

app_name='core_api'

urlpatterns = [
    path ('starwars_test', charTest),
    path('character/<int:id>', get_char_by_id),
]
