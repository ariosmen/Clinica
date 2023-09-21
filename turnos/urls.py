from django.urls import path
from turnos import views

urlpatterns = [
    path('registrar_turnos/<int:pac>', views.registrar_turnos, name='registrar_turnos'),
    path('eliminar_turnos/<int:turno>/<int:paciente>', views.eliminar_turnos, name='eliminar_turnos'),
    path('editar_turnos/<int:turno>/<int:paciente>', views.editar_turnos, name='editar_turnos'),
]


