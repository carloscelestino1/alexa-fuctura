from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['data', 'descricao', 'link']