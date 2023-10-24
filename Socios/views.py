from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Socio
from .forms import SocioForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
# Create your views here.

     
class SociosListView(ListView):
    model = Socio
    context_object_name= "lista_socios"   
    template_name = 'socios/socios.html'


    
class DetalleSocio(DetailView):
    model = Socio
    context_object_name = 'detalle_socio'

class CrearSocio(CreateView):
    model = Socio   
    form_class = SocioForm
    template_name = 'socios/crear_socio.html'
    success_url = reverse_lazy('lista_socios')

class EditarSocio(UpdateView):
    model = Socio
    form_class= SocioForm
    template_name = 'socios/editar_socio.html'  
    success_url = reverse_lazy("lista_socios")
    


class EliminarSocio(DeleteView):
    model = Socio
    template_name = 'socios/eliminar_socio.html'
    success_url = reverse_lazy("lista_socios")


