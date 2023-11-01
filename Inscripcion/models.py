from django.db import models
from Socios.models import Socio
from Administracion.models import Actividad, Categoria

# Create your models here.
class Inscripcion(models.Model):

    socio=models.ForeignKey(Socio, verbose_name="Socio", on_delete=models.CASCADE, null=False)
    actividad=models.ForeignKey(Actividad, verbose_name="Actividad", on_delete=models.CASCADE, null=False)
    categoria=models.ForeignKey(Categoria, verbose_name="Categoria", on_delete=models.CASCADE, null=False)
    fecha_inscripcion = models.DateField(auto_now_add=True,verbose_name='Fecha de Inscripcion', null=False)
    
    def __str__(self):
        return f"Inscripción de {self.socio} en {self.actividad} - {self.categoria}"
