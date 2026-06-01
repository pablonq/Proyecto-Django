from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración de Django
    path('', include('miApp.urls')),  # Incluye las rutas definidas en la app miApp
    path('__reload__/', include('django_browser_reload.urls')),  # Ruta para recarga en caliente en desarrollo
]
