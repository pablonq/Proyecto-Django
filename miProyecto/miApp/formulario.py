from django.forms import ModelForm
from .models import post

class FormularioPost(ModelForm):
    class Meta: 
        model = post
        fields = ['titulo', 'contenido']

