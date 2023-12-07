from .models import ObraDeArte
from rest_framework import serializers

class ObraDeArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObraDeArte
        fields = '__all__'
    