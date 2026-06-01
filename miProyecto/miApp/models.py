from django.db import models
from django.contrib.auth.models import User

# Modelos del proyecto

class usuario(models.Model):
    """Modelo para representar un usuario con datos personales."""
    nombre = models.CharField(max_length=100)  # Nombre completo del usuario
    dni = models.IntegerField()  # Número de documento de identidad
    telefono = models.CharField(max_length=15)  # Teléfono de contacto
    perfil = models.TextField()  # Descripción del perfil del usuario
    email = models.EmailField()  # Email del usuario
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha en que se creó el registro

    def __str__(self):
        # Representación legible del objeto en el admin y otros contextos
        return self.nombre


class post(models.Model):
    """Modelo para representar un post en el blog."""
    titulo = models.CharField(max_length=200)  # Título del post
    contenido = models.TextField()  # Contenido de texto completo del post
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor relacionado al usuario de Django
    fecha_publicacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        # Muestra el título del post como representación del objeto
        return self.titulo

   