from django.urls import path
from especialidades import views

urlpatterns = [
    path('especialidades/', views.especialidades, name='especialidades'),
    path('eliminar_especialidad/<int:esp>', views.eliminar_especialidad, name='eliminar_especialidad'),
    path('editar_especialidad/<int:esp>', views.editar_especialidad, name='editar_especialidad'),
]
