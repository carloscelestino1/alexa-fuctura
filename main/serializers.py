from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Agenda

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['descricao',]