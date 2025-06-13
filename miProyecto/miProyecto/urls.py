
from django.contrib import admin
from django.urls import path, include
from miApp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('miApp.urls')),
    path("__reload__/", include("django_browser_reload.urls"))
        # Incluye las URLs de miApp
]
