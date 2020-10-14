import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

def charTest(request):
    if request.method == "GET": 
        response = requests.get('https://swapi.dev/api/people/1/')
        char = response.json()
        return HttpResponse(response, content_type="application/json")
    
      

