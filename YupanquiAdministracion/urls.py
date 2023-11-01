"""
URL configuration for YupanquiAdministracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('socios/', include("Socios.urls")),    
    path('administracion/',include("Administracion.urls")), 
    path('cuotas/', include("Cuotas.urls")),
    # path('inscripciones/', include("inscripciones.urls")) , 
    path('accounts/', include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)