from django.test import TestCase
from rest_framework import status

from core_api.views import get_character
from core_api.models import Character

import requests

class TestApi(TestCase):
    """Clase para testear funciones para la api"""
    
    def setUp(self):
        self.client = requests

    def test_get_success_char(self):
        """Test request al endpoint para char de la API"""
        url = "https://swapi.dev/api/people"
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_success_homeworld(self):
        """Test request al endpoint para homeworld de la API"""
        url = "https://swapi.dev/api/planets"
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_success_species(self):
        """Test request al endpoint para species de la API"""
        url = "https://swapi.dev/api/people"
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_character_by_id(self):
        """Test con la request de people con id 1, como referencia la documentacion de la API"""
        url = "https://swapi.dev/api/people/1"
        res = self.client.get(url)
        
        resp = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn(resp['name'], "Luke Skywalker")

    def test_get_planet_by_id(self):
        """Test con la request de planet con id 1, como referencia la documentacion de la API"""
        url = "https://swapi.dev/api/planets/1"
        res = self.client.get(url)
        
        resp = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn(resp['name'], "Tatooine")
    
    def test_get_species_by_id(self):
        """Test con la request de species con id 1, como referencia la documentacion de la API"""
        url = "https://swapi.dev/api/species/1"
        res = self.client.get(url)
        
        resp = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn(resp['name'], "Human")