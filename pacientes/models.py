from django.db import models
from pacientes.opciones import SEXO, ESTADO_CIVIL

class Paciente(models.Model):
    
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='DNI')
    sexo = models.CharField(choices=SEXO, max_length=10, verbose_name='Sexo')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    telefono = models.CharField(max_length=50, verbose_name='Telefono')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email')
    estado_civil = models.CharField(max_length=50, choices=ESTADO_CIVIL, verbose_name='Estado Civil')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nac.')
    obra_social = models.CharField(null=True, blank=True, max_length=50)
    activo = models.BooleanField(verbose_name='Estado', default=True)
    create = models.DateField(auto_now_add=True, verbose_name='Fecha de registro')

    class Meta:
        db_table = 'pacientes'
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
        ordering = ['apellido', 'nombre']
        
    def __str__(self):
        return self.apellido + ' ' + self.nombre
    
