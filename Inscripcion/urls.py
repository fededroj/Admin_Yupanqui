from django.urls import path
from .views import   BuscarSocio, CrearIncripcion, InscripcionDetailView

urlpatterns = [

    path('', BuscarSocio.as_view(), name='index_inscripcion'),  
       
    path('inscribir/<int:socio_id>', CrearIncripcion.as_view(), name='inscripcion'),
    
    path('detail/<int:pk>', InscripcionDetailView.as_view(), name='detail_inscripcion' ),
]