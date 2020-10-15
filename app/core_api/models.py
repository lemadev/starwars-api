from django.db import models

class Character(models.Model):
    """Clase para character de star wars API"""
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    mass = models.IntegerField()
    hair_color = models.CharField(max_length=50)
    skin_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    homeworld = models.CharField(max_length=255)
    species = models.CharField(max_length=50)
    average_rating = models.DecimalField(max_digits=5, decimal_places=2)
    max_rating = models.DecimalField(max_digits=5, decimal_places=2)
