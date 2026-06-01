from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta principal del sitio
    path('about/', views.about, name='about'),  # Página estática de información
    path('posts/', views.posts, name='posts_list'),  # Lista de posts
    path('posts/<int:post_id>', views.post_detail, name='post_detail'),  # Detalle de un post por id
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),  # Editar un post existente
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),  # Eliminar un post existente
    path('register/', views.register, name='register'),  # Registro de nuevos usuarios
    path('login/', views.login_view, name='login'),  # Inicio de sesión
    path('logout/', views.logout_view, name='logout'),  # Cierre de sesión
    path('posts/crear/', views.post_create, name='post_create'),  # Crear un nuevo post
]

