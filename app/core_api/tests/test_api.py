from django.test import TestCase

from rest_framework import status
from rest_framework.test import RequestsClient, APIClient

API_URL = "https://swapi.dev/api/people/"

class TestApi(TestCase):
    """Clase para testear funciones para la api"""
    
    def setUp(self):
        self.client = RequestsClient()

    def test_get_success(self):
        """Check que el endpoint este activo"""
        res = self.client.get(API_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)