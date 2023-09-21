from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico
from especialidades.models import Especialidad
from turnos.opciones import HORARIOS

class Turno(models.Model):
    
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.CharField(choices=HORARIOS, max_length=50, verbose_name='Hora')
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, verbose_name='Medico', on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, verbose_name='Especialidad', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        db_table = 'Turnos'
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        