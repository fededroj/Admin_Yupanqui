
from django.urls import path
from . import views 



urlpatterns =[
   
    path('',views.SociosListView.as_view(),name='lista_socios'),
    path('detalle_socio/<int:pk>', views.DetalleSocio.as_view(), name="detalle_socio"),
    path('crear_socio',views.CrearSocio.as_view(), name='crear_socio'),
    path('editar_socio/<int:pk>',views.EditarSocio.as_view(), name="editar_socio"),
    path('eliminar_socio/<int:pk>', views.EliminarSocio.as_view(), name="eliminar_socio"),  
    path('buscar',views.BuscarSocioView.as_view(), name="buscar_socio") , 

    path('registrar_cuota/<int:pk>', views.CuotaCreateView.as_view(), name='registrar_cuota')
]