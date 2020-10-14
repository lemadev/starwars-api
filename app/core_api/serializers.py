from rest_framework import serializers

from core_api.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    """Serializer for tags object"""

    class Meta:
        model = Character
        fields = ('id', 'name', 'height', 'mass')
        read_only_fields = ('id',)