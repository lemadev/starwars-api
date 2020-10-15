from django.db import models

class Character(models.Model):
    """Clase para character de star wars API"""
    ranking = models.IntegerField()
    id_character = models.IntegerField()
