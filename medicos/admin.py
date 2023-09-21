from django.contrib import admin
from medicos.models import Medico

admin.site.site_header = "Administracion de la Clinica"

class MedicoAdmin(admin.ModelAdmin):
    # inlines = (EspacialidadMedicoInline, )
    search_fields = ('nombre', 'apellido', )
    list_display = ('nombre', 'apellido', )
    
admin.site.register(Medico, MedicoAdmin)
