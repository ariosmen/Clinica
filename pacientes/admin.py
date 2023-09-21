from django.contrib import admin
from pacientes.models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'create', 'activo', )
    search_fields = ('nombre', 'apellido', 'dni', )
    
admin.site.register(Paciente, PacienteAdmin)