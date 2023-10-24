from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Profesor, Actividad, Categoria
from .forms import ProfesorForm, ActividadForm, CategoriaForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView 

class Index(TemplateView):
    def get(self, request ,*args,**kwargs):
        return render(request, "administracion/index.html")



# Create your views here.
#VISTA DE PROFESORES

class ProfesoresListView(ListView):
    model = Profesor
    paginate_by = 15
    context_object_name = 'profesores'
    template_name = 'administracion/profesores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
class DetalleProfesor(DetailView):
    model = Profesor
    context_object_name = 'detalle_profesor'

class CrearProfesor(CreateView):
    model = Profesor
   
    form_class = ProfesorForm
    template_name = 'administracion/crear_profesor.html'
    success_url = reverse_lazy('lista_profesores')

class EditarProfesor(UpdateView):
    model = Profesor
    form_class= ProfesorForm
    template_name = 'administracion/editar_profesor.html'  
    success_url = reverse_lazy("lista_profesores")
    


class EliminarProfesor(DeleteView):
    model = Profesor
    template_name = 'administracion/eliminar_profesor'
    success_url = reverse_lazy('administracion : profesores')



 #ACTIVIDADES
class ActividadesListView(ListView):
    model = Actividad
    context_object_name = 'actividades'
    template_name = 'administracion/actividades.html'

    

class DetalleActividad(DetailView):
    model= Actividad
    context_object_name= 'detalle_actividad'

class CrarActividad(CreateView):
    
    model = Actividad
    form_class = ActividadForm
    template_name = 'administracion/crear_actividad.html'  
    
    success_url = reverse_lazy('lista_actividades')

class EditarActividad(UpdateView):

    model = Actividad
    form_class= ActividadForm
    template_name = 'administracion/editar_actividad.html'  
    success_url = reverse_lazy("lista_actividades")
    

class EliminarActividad(DeleteView):
    model = Actividad
    template_name = 'administracion/eliminar_actividad.html'
    success_url = reverse_lazy('lista_actividades')




#Categorias
class CategoriasListView(ListView):
    model = Categoria
    paginate_by = 15
    context_object_name="categorias"
    template_name = 'administracion/categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class CrearCategoria(CreateView):
    model = Categoria
    form_class= CategoriaForm
    template_name = 'administracion/crear_categoria.html'  

    success_url =reverse_lazy("lista_categorias")

class EditarCategoria(UpdateView):
    model = Categoria
    form_class= CategoriaForm
    template_name = 'administracion/editar_categoria.html'  
    success_url = reverse_lazy("lista_categoria")
   

class BorrarCategoria(DeleteView):
    model= Categoria
    template_name ="administracion/borrar_categoria.html"
    success =reverse_lazy("lista_categorias")
    

class DetalleCategoria(DetailView):
    model= Categoria
    context_object_name= 'detalle_categoria'

class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'administracion/eliminar_categoria.html'
    success_url = reverse_lazy('lista_categorias')