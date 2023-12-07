from django.shortcuts import render

# Create your views here.

from .models import LojaMuseu
from rest_framework import viewsets
from .serializer import LojaMuseuSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = LojaMuseu.objects.all()
    serializer_class = LojaMuseuSerializer
    