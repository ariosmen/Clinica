from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico

class HistoriaClinica(models.Model):
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=2000, verbose_name='Descripcion', null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'hisotira clinica'
        verbose_name = 'Historia Clinica'
        verbose_name_plural = 'Historias Clinicas'
    
    def __str__(self):
        return self.descripcion
        