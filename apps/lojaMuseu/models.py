from django.db import models

from obraDeArte.models import ObraDeArte

# Create your models here.

class LojaMuseu(models.Model):
    name = models.CharField('Nome da Obra:', max_length=100)
    valor = models.CharField('Valor da Obra:', max_length=50)
    quantidade = models.TextField('Quantidade disponivel:', max_length=10)
    obraDeArte = models.ForeignKey(ObraDeArte, on_delete=models.CASCADE, default=0)
    
    class Meta:
        verbose_name = 'LojaMuseu'
        verbose_name_plural = 'LojaMuseu'
        ordering =['id']

    def __str__(self):
        return self.name