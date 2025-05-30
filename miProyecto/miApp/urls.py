from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),  # Página de inicio
  path('about/', views.about),  # Página "Acerca de"
  path('posts/', views.posts),  # Página de posts
]

