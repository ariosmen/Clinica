from django.db import models
from medicos.opciones import SEXO, ESTADO_CIVIL
from especialidades.models import Especialidad

class Medico(models.Model):
    
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='DNI')
    sexo = models.CharField(choices=SEXO, max_length=10, verbose_name='Sexo')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    telefono = models.CharField(max_length=50, verbose_name='Telefono')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email')
    estado_civil = models.CharField(max_length=50, choices=ESTADO_CIVIL, verbose_name='Estado Civil')
    fecha_nacimiento = models.DateField(null=True, verbose_name='Fecha de Nac.')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    activo = models.BooleanField( verbose_name='Estado', default=True) 
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'medicos'
        verbose_name = 'medico'
        verbose_name_plural = 'medicos'
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido

