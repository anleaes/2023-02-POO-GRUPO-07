from .models import LojaMuseu
from rest_framework import serializers

class LojaMuseuSerializer(serializers.ModelSerializer):
    class Meta:
        model = LojaMuseu
        fields = '__all__'
    