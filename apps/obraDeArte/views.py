from django.shortcuts import render

# Create your views here.

from .models import ObraDeArte
from rest_framework import viewsets
from .serializer import ObraDeArteSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class ObraDeArteViewSet(viewsets.ModelViewSet):
    queryset = ObraDeArte.objects.all()
    serializer_class = ObraDeArteSerializer
    