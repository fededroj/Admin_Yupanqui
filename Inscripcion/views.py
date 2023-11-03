from django.shortcuts import render
from.models import Inscripcion
from Socios.models import Socio
from.forms import InscripcionForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView 
from django.views.generic import DetailView
# Create your views here.


class BuscarSocio(ListView):
    model = Socio
    template_name = 'inscripcion/buscar.html'
    context_object_name = 'socios'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Socio.objects.filter(nroSocio__icontains=query) | Socio.objects.filter(apellido__icontains=query) | Socio.objects.filter(nombre__icontains=query)
        return Socio.objects.all()
    
class CrearIncripcion(CreateView):
 
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'inscripcion/crear_inscripcion.html'
    success_url= reverse_lazy("index_inscripcion")

    def get_initial(self):
      #  Obtiene el ID del socio desde la URL (debes configurar la URL en consecuencia)
        socio_id = self.kwargs.get('socio_id')
        return {'socio': socio_id}

class InscripcionDetailView(DetailView):
    model = Inscripcion
    template_name = 'inscripcion/inscripcion_detail.html'  # Nombre de la plantilla HTML que has creado.
    context_object_name = 'inscripcion'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['socio'] = Socio.objects.get(inscripcion=self.object)  # Accede al socio relacionado.
        return context