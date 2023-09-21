from django.urls import path
from pacientes import views

urlpatterns = [
    path('pacientes/', views.pacientes, name='pacientes'),
    path('registrar_paciente/', views.registrar_paciente, name='registrar_paciente'),
    path('eliminar_paciente/<int:paciente>', views.eliminar_paciente, name='eliminar_paciente'),
    path('editar_paciente/<int:paciente>', views.editar_paciente, name='editar_paciente'),
    path('busqueda/', views.busqueda, name='busqueda'),
]
