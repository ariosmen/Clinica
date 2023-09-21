from django.urls import path
from medicos import views

urlpatterns = [
    path('medicos/', views.medicos, name='medicos'),
    path('registrar_medico/', views.registrar_medico, name='registrar_medico'),
    path('eliminar_medico/<int:medico>', views.eliminar_medico, name='eliminar_medico'),
    path('editar_medico/<int:medico>', views.editar_medico, name='editar_medico'),
]
