from django.urls import path
from historiaclinica import views

urlpatterns = [
    path('historiaclinica/<int:hc>', views.historiaclinica, name='historiaclinica'),
    path('ingreso/<int:hc>', views.ingreso, name='ingreso'),
    path('editar_hc/<int:hc>/<int:pac>', views.editar_hc, name='editar_hc'),
    path('eliminar_hc/<int:hc>/<int:pac>', views.eliminar_hc, name='eliminar_hc'),
]
