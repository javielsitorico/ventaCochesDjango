from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre  = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')    

    class Meta:
        verbose_name='categoria'
        verbose_name_plural="categorias"
        ordering=['-created']

    def __str__(self):
        return self.nombre

class Coche(models.Model):
    marca = models.CharField(max_length=200)
    modelo  = models.CharField(max_length=200)
    kilometros = models.IntegerField()
    descripcion = models.TextField()
    precio = models.FloatField()
    imagen = models.ImageField(verbose_name='foto coche',upload_to='coches')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria,verbose_name="categoria")
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación ')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='coche'
        verbose_name_plural="coches"
        ordering=['-created']

    def __str__(self):
        return self.modelo