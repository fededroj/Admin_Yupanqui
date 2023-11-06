from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Socio
from .forms import SocioForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class LoginFormView(LoginView):
    template_name="login.html"

    # def get_context_data(self, **kwargs) :
    #     context = super().get_context_data(**kwargs)
    #     context['title']= "LoginFormView"
    #     return context

    




class BuscarSocioView(LoginRequiredMixin,ListView):
    model = Socio
    template_name = 'socios/index_socios.html'
    context_object_name = 'socios'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Socio.objects.filter(nroSocio__icontains=query) | Socio.objects.filter(apellido__icontains=query)
        return Socio.objects.all()
    
class DetalleSocio(LoginRequiredMixin,DetailView):
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


