from django.contrib import admin
from turnos.models import Turno

class TurnoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'hora', )

admin.site.register(Turno, TurnoAdmin)