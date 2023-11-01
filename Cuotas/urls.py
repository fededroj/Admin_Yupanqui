from django.urls import path
from .views import   BuscarSocio, PagoCuotaCreateView, CuotasAnualesListView, PagoCuotaActCreateView

urlpatterns = [

    path('', BuscarSocio.as_view(), name='index_cuotas'),    
    # path('lista_cuotas/<int:socio_id>/', ReporteCuotasAnualesView.as_view(), name='lista_cuotas'),    
    path('pago_cuota/<int:socio_id>', PagoCuotaCreateView.as_view(), name='pago_cuota'),
    path('cuotas_anuales/<int:socio_id>/', CuotasAnualesListView.as_view(), name='cuotas_anuales'),
    path('pago_actividad/<int:socio_id>/', PagoCuotaActCreateView.as_view(), name='pago_cuota_act'),

   
]