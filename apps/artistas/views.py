from django.shortcuts import render

# Create your views here.

from .models import Artista
from rest_framework import viewsets
from .serializer import ArtistaSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    