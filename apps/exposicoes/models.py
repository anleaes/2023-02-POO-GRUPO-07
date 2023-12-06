from django.db import models

from artistas.models import Artista

# Após o comentario "# Create your models here." e crie a classe "Product" do modelo.

class exposicao(models.Model):
    nome = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    data_exposicao = models.DateField('Data Exposição', auto_now=False, auto_now_add=False) 
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Exposição'
        verbose_name_plural = 'Exposições'
        ordering =['id']

    def __str__(self):
        return self.name