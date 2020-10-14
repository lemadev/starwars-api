import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

    
def get_char_by_id(request, id):
    if request.method == "GET":
        url =  "https://swapi.dev/api/people/"+str(id)+"/"
        response = requests.get(url)
        char = response.json()
        return HttpResponse(response, content_type="application/json")
      

