from django import forms
from .models import  Actividad, Profesor, Categoria, Inscripcion


class ActividadForm(forms.ModelForm):
     class Meta:

        model = Actividad
        fields =['nombre', 'categoria']
        widget ={
        'categoria' : forms.CheckboxSelectMultiple
    }

# class ActividadForm(forms.ModelForm):

#      class Meta:
#           model = Actividad
#           fields = '__all__'

class ProfesorForm(forms.ModelForm):

     class Meta:
          model = Profesor
          fields = '__all__'

class CategoriaForm(forms.ModelForm):

     class Meta:
          model = Categoria
          fields = '__all__'

class InscripcionForm(forms.ModelForm):
     
     class Meta:
          model = Inscripcion
          fields = '__all__'