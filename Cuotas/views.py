from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView,  TemplateView
from .models import CuotaMensual, CuotaActividad
from .forms import CuotaMensualForm, CuotaActividadForm
from django.urls import reverse_lazy
from Socios.models import Socio
from django.shortcuts import render
from .forms import YearFilterForm

# index buscador con lista de socios
class BuscarSocio(ListView):
    model = Socio
    template_name = 'socios/buscar.html'
    context_object_name = 'socios'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Socio.objects.filter(nroSocio__icontains=query) | Socio.objects.filter(apellido__icontains=query) | Socio.objects.filter(nombre__icontains=query)
        return Socio.objects.all()
    


# class ReporteCuotasAnualesView(TemplateView):
#     template_name = 'lista_cuotas.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Obtener el año seleccionado desde la URL
#         selected_ano = self.request.GET.get('year', None)
#         context['selected_ano'] = selected_ano

#         # Filtrar cuotas por año y por socio
#         cuotas = CuotaMensual.objects.filter(fecha_pago__year=selected_ano, socio=context['socio_id'])
#         context['cuotas'] = cuotas
#         return context

class PagoCuotaCreateView(CreateView):
    model = CuotaMensual
    form_class = CuotaMensualForm
    template_name = 'cuotas/cuota_form.html'

    def get_initial(self):
        # Obtiene el ID del socio desde la URL (debes configurar la URL en consecuencia)
        socio_id = self.kwargs.get('socio_id')
        return {'socio': socio_id}

    def form_valid(self, form):
        # Personaliza la lógica después de que el formulario sea válido
        # Puedes agregar validaciones adicionales o realizar otras acciones aquí
        return super().form_valid(form)
    success_url= reverse_lazy("index_cuotas")

class CuotasAnualesListView(ListView):
    model = CuotaMensual  # Especifica el modelo a utilizar
    template_name = 'cuotas/cuotas_anuales.html'
    context_object_name = 'cuotas'  # Nombre del objeto en el contexto

    def get_queryset(self):
        # Obtén el ID del socio desde los parámetros de la URL
        socio_id = self.kwargs.get('socio_id')
        # Filtra las cuotas para el socio y el año seleccionado en el formulario
        ano = self.request.GET.get('ano')
        queryset = CuotaMensual.objects.filter(socio__id=socio_id, ano=ano)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = YearFilterForm()
        # Obtén el ID del socio desde los parámetros de la URL
        context['socio_id'] = self.kwargs.get('socio_id')
        return context


# CUOTAS DE ACTIVIDADES
# Regitro cuota Actividad
class PagoCuotaActCreateView(CreateView):
    model = CuotaActividad
    form_class = CuotaActividadForm
    template_name = 'cuotas/cuota_actividad.html'

    def get_initial(self):
        # Obtiene el ID del socio desde la URL (debes configurar la URL en consecuencia)
        socio_id = self.kwargs.get('socio_id')
        return {'socio': socio_id}

    def form_valid(self, form):
        # Personaliza la lógica después de que el formulario sea válido
        # Puedes agregar validaciones adicionales o realizar otras acciones aquí
        return super().form_valid(form)
    success_url= reverse_lazy("index_cuotas")


