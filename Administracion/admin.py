from django.contrib import admin
#admin de modelos
from .models import *
from Socios.models import Socio



# Register your models here.
admin.site.register(Socio)
