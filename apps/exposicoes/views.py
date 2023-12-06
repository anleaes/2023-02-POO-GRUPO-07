from django.shortcuts import render

# Create your views here.

from .models import exposicao
from rest_framework import viewsets
from .serializer import ExposicaoSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class ExposicaoViewSet(viewsets.ModelViewSet):
    queryset = exposicao.objects.all()
    serializer_class = ExposicaoSerializer
