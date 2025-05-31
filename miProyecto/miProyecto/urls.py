
from django.contrib import admin
from django.urls import path, include
from miApp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('miApp.urls')),
        # Incluye las URLs de miApp
]
