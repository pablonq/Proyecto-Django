from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField()
    telefono = models.CharField(max_length=15)
    perfil = models.TextField()
    email = models.EmailField()
  
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

   