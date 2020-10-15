from rest_framework import serializers
from core_api.models import Character


class CharacterModelSerializer(serializers.ModelSerializer):
    """Serializer character object"""
    average_rating = serializers.DecimalField(required=False, max_digits=5, decimal_places=2)
    max_rating = serializers.DecimalField(required=False, max_digits=5, decimal_places=2)
    class Meta:
        model = Character
        fields = ('name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color','birth_year', 'homeworld', 'gender',
                  'species', 'average_rating', 'max_rating')
    

class CharacterSerializer(serializers.Serializer):
    """Custom serializer for character"""
    name = serializers.CharField(max_length=200)
    height = serializers.IntegerField()
    mass = serializers.IntegerField()
    hair_color = serializers.CharField(max_length=200)
    skin_color = serializers.CharField(max_length=200)
    eye_color = serializers.CharField(max_length=200)
    birth_year = serializers.CharField(max_length=200)
    gender = serializers.CharField(max_length=200)
    homeworld = serializers.CharField(max_length=255)
    species = serializers.CharField(max_length=200)
    average_ratinge = serializers.DecimalField(required=False, max_digits=5, decimal_places=2)
    max_rating = serializers.DecimalField(required=False, max_digits=5, decimal_places=2)