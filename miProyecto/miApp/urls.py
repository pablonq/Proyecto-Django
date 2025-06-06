from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),  # Página de inicio
  path('about/', views.about),  # Página "Acerca de"
  path('posts/', views.posts, name='posts_list'), # Página de posts
  path('posts/<int:post_id>', views.post_detail, name='post_detail'), # Detalle de un post específico
  path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),  # Editar un post específico
  path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),  # Eliminar un post específico
  path('register/', views.register, name='register'),  # Página de inicio de registro
  path('login/', views.login_view, name='login'),  # Página de inicio de sesión
  path('logout/', views.logout_view, name='logout'),  # Página de cierre de sesión
  path('posts/crear/', views.post_create, name='post_create'),  # Crear un nuevo post
  
]

