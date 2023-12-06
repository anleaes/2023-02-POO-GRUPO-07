from django.shortcuts import render

# Create your views here.

from .models import Exposicao
from rest_framework import viewsets
from .serializer import ExposicaoSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class ExposicaoViewSet(viewsets.ModelViewSet):
    queryset = Exposicao.objects.all()
    serializer_class = ExposicaoSerializer
