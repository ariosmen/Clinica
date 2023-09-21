from django.db import models

class Especialidad(models.Model):
    
    especialidad = models.CharField(max_length=50, unique=True, verbose_name='Especialidad')
    create = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'especialidades'
        verbose_name = 'especialidad'
        verbose_name_plural = 'especialidades'
        ordering = ['especialidad']

    def __str__(self):
        return self.especialidad
