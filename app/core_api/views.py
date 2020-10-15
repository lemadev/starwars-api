import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json

def get_character(request, id):
    if request.method == "GET":
        url =  "http://swapi.dev/api/people/"+str(id)+"/"
        url_home = "http://swapi.dev/api/planets/1/"
        response = requests.get(url)
        resp = response.json()
        if resp['homeworld']:
            resp['homeworld'] = get_homeworld(resp['homeworld'])
        if resp['species']:
            resp['species'] = get_specie(resp['species'])
        respuesta = json.dumps(resp)
        if response.status_code == 200:
            return HttpResponse(respuesta, content_type="application/json")
        else:
            return HttpResponse('No hay valores para el id ingresado')

def get_homeworld(url_planet):
    response = requests.get(url_planet)
    resp = response.json()
    valores_homeworld = {'name':resp['name'], 'population':resp['population'],
    'know_residents_count':len(resp['residents'])}
    return valores_homeworld
    
def get_specie(url_specie):
    response = requests.get(url_specie)
    resp = response.json()
    return resp['name']
