from django.shortcuts import render

# Create your views here.

from .models import Comprador
from rest_framework import viewsets
from .serializer import CompradoresSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Comprador.objects.all()
    serializer_class = CompradoresSerializer
    