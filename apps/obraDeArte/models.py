from django.db import models

# Create your models here.

class ObraDeArte(models.Model):
    name = models.CharField('Nome', max_length=50)
    Artista = models.CharField('Artista', max_length=50)
    valor = models.TextField('valor', max_length=100)
    
    class Meta:
        verbose_name = 'ObraDeArte'
        verbose_name_plural = 'ObraDeArte'
        ordering =['id']

    def __str__(self):
        return self.name