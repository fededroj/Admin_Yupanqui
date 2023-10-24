from django.db import models
from Socios.models import Socio
from Administracion.models import Actividad
from Administracion.models import Categoria

class Inscripcion(models.Model):

    nroSocio=models.ForeignKey(Socio, verbose_name="Nro Socio", on_delete=models.CASCADE, null=False)
    actividad=models.ForeignKey(Actividad, verbose_name="Actividad", on_delete=models.CASCADE, null=False)
    categoria=models.ForeignKey(Categoria, verbose_name="Categoria", on_delete=models.CASCADE, null=False)
    fecha_inscripcion = models.DateField(auto_now_add=True,verbose_name='Fecha de Inscripcion', null=False)
    
