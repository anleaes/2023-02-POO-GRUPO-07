from .models import Comprador
from rest_framework import serializers

class CompradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = '__all__'
    