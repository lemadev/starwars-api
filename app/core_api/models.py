from django.db import models

class Character(models.Model):
    """Clase para character de star wars API"""
    id_personaje = models.IntegerField()
    rating = models.IntegerField()
