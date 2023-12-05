from django.shortcuts import render
from .models import Visitante
from rest_framework import viewsets
from .serializer import VisitanteSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer  
