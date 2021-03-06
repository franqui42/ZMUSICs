from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)

class Album (models.Model):
    artista = models.CharField(max_length=100)
    nombre = models.CharField(max_length=500)
    descripcion = models.TextField(max_length=500)
    año = models.IntegerField()
    foto = models.ImageField(upload_to='album',null=True,blank=True)
    genero = models.ManyToManyField(Genero)
   
    def __str__(self):
        return self.nombre + ' '+ str(self.año)