

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Socio
from .forms import SocioForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from Cuotas.models import CuotaMensual
from Cuotas.forms import CuotaMensualForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

     

class BuscarSocioView(ListView):
    model = Socio
    template_name = 'socios/index_socios.html'
    context_object_name = 'socios'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Socio.objects.filter(nroSocio__icontains=query) | Socio.objects.filter(apellido__icontains=query)
        return Socio.objects.all()
    
class DetalleSocio(DetailView):
    model = Socio
    context_object_name = 'detalle_socio'

class CrearSocio(CreateView):
    model = Socio   
    form_class = SocioForm
    template_name = 'socios/crear_socio.html'
    success_url = reverse_lazy('index_socios')

class EditarSocio(UpdateView):
    model = Socio
    form_class= SocioForm
    template_name = 'socios/editar_socio.html'  
    success_url = reverse_lazy("index_socios")
    


class EliminarSocio(DeleteView):
    model = Socio
    template_name = 'socios/eliminar_socio.html'
    success_url = reverse_lazy("index_socios")


