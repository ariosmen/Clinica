from django.contrib import admin
from especialidades.models import Especialidad

admin.site.site_header = "Administracion de la Clinica"

class EspecialidadAdmin(admin.ModelAdmin):
    # inlines = (EspacialidadMedicoInline, )
    # search_fields = ('especialidad', )
    list_display = ('especialidad', )

admin.site.register(Especialidad, EspecialidadAdmin)
