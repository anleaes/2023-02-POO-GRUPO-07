from django.db import models

from exposicoes.models import Exposicao

# Create your models here.

class Visitante(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    rg = models.IntegerField('rg' ,max_length=10)
    exposicao = models.ForeignKey(Exposicao, on_delete=models.CASCADE, default=0)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name
