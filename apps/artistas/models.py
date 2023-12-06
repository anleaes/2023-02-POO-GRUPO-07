from django.db import models

# Create your models here.

class Artista(models.Model):
    name = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    biografia = models.TextField('biografia', max_length=100)
    
    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering =['id']

    def __str__(self):
        return self.name