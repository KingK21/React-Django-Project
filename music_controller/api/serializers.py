from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        models = Room
        fields = ('id', 'code', 'host', 'pause_to_status','votes_to_skip', 'created_at')