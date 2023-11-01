from django import forms
from .models import CuotaMensual, CuotaActividad


class CuotaMensualForm(forms.ModelForm):
    class Meta:
        model = CuotaMensual
        fields = [ 'socio', 'mes', 'ano','monto', 'fecha_pago']

class CuotaActividadForm(forms.ModelForm):
    
    class Meta:
        model = CuotaActividad
        fields = ('__all__')


class YearFilterForm(forms.Form):
    ano = forms.ChoiceField(choices=[(str(ano), str(ano)) for ano in range(2022, 2030)], label='Año')