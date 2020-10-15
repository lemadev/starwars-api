import requests
from django.http import HttpResponse
from django.shortcuts import render
from core_api.serializers import CharacterSerializer, CharacterModelSerializer
import json

def get_character(request, id):
    #funciona con serializer comun
    if request.method == "GET":
        url =  "http://swapi.dev/api/people/"+str(id)+"/"
        response = requests.get(url)
        if response.status_code == 200:
            resp = response.json()
            if resp['homeworld']:
                resp['homeworld'] = get_homeworld(resp['homeworld'])
            if resp['species']:
                resp['species'] = get_specie(resp['species'])
            char = CharacterModelSerializer(resp)
            respuesta = json.dumps(char.data)
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
    print(url_specie[0])
    url = url_specie[0]
    response = requests.get(url)
    resp = response.json()
    return resp['name']
