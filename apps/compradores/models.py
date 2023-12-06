from django.db import models

# Create your models here.

class Comprador(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    cpf = models.TextField('CPF', max_length=11)
    historico_compras = models.TextField('Historico de compras:', max_length=100)
    
    class Meta:
        verbose_name = 'Compradores'
        verbose_name_plural = 'Compradores'
        ordering =['id']

    def __str__(self):
        return self.name