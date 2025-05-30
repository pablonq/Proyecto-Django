
from django.http import HttpResponse
from django.shortcuts import render
from .models import post  # Importa el modelo post

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def posts(request):
    posts = post.objects.all()  # Obtiene todos los posts de la base de datos
    return render(request, 'posts.html',{
        'posts': posts  # Pasa los posts al contexto de la plantilla
    })  


