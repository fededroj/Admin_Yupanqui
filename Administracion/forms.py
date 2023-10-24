from django import forms
from .models import  Actividad, Profesor, Categoria




class ActividadForm(forms.ModelForm):

     class Meta:
          model = Actividad
          fields = '__all__'

class ProfesorForm(forms.ModelForm):

     class Meta:
          model = Profesor
          fields = '__all__'

class CategoriaForm(forms.ModelForm):

     class Meta:
          model = Categoria
          fields = '__all__'
