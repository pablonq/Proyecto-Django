from django.forms import ModelForm
from .models import post

class FormularioPost(ModelForm):
    """Formulario basado en el modelo post para crear y editar entradas."""

    class Meta:
        model = post
        fields = ['titulo', 'contenido']  # Campos que se mostrarán en el formulario

