from django.shortcuts import render

# Create your views here.

from .models import Compradores
from rest_framework import viewsets
from .serializer import ArtistaSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Compradores.objects.all()
    serializer_class = CompradoresSerializer
    