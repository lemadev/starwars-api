import requests
from django.http import HttpResponse
from core_api.serializers import CharacterSerializer
from core_api.models import  Character
from rest_framework import status
import json

def post_character(request, id, rating):
    if request.method == "POST":
            character = Character(id_personaje=id, rating=rating)
            character.save()
            return HttpResponse({"success": "Request successful"},status=status.HTTP_200_OK)
    else:
        return HttpResponse({"error": "Request failed"})
        
def get_character(request, id):
    hay_chars = Character.objects.all()
    if request.method == "GET":
        url =  "http://swapi.dev/api/people/"+str(id)+"/"
        response = requests.get(url)
        if response.status_code == 200:
            resp = response.json()
            if resp['homeworld']:
                resp['homeworld'] = get_homeworld(resp['homeworld'])
            if resp['species']:
                resp['species'] = get_specie(resp['species'])
            if hay_chars:
                ratings = get_ratings(hay_chars)
                resp['average_rating'] = ratings['average_rating']
                resp['max_rating'] = ratings['max_rating']
            char = CharacterSerializer(resp)
            respuesta = json.dumps(char.data)
            return HttpResponse(respuesta, status=status.HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse({"error": "Request failed"}, status=response.status_code)
    else:
        return HttpResponse({"error": "Request failed"})

def get_homeworld(url_planet):
    """Obtengo datos del planeta del character"""
    response = requests.get(url_planet)
    resp = response.json()
    valores_homeworld = {'name':resp['name'], 'population':resp['population'],
    'know_residents_count':len(resp['residents'])}
    return valores_homeworld
    
def get_specie(url_specie):
    """Obtengo el nombre de la especie para el character"""
    url = url_specie[0] #Saco [] del string
    response = requests.get(url)
    resp = response.json()
    return resp['name']

def get_ratings(chars):
    """Obtengo los datos de max_rating y average_rating"""
    sum = 0
    max = 0
    for char in chars:
        rating = char.rating
        sum = sum + rating
        if rating>max:
            max = rating
    average = (sum/chars.count())
    return {'average_rating':average, 'max_rating':max}


