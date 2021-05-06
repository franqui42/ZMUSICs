from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)

class Album (models.Model):
    artista = models.CharField(max_length=100)
    nombre = models.CharField(max_length=500)
    descripcion = models.TextField(max_length=500)
    año = models.IntegerField(max_length=100)
    genero = models.ManyToManyField(Genero,null=True,blank=True)
   
    def __str__(self):
        return self.nombre + ' '+ str(self.año)