from rest_framework import serializers
from .models import tablero_model

class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = tablero_model
        fields = ['id', 'guia', 'recibio', 'lista', 'cliente', 'desc', 'imagen', 'fecha_recepcion']