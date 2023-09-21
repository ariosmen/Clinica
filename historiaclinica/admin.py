from django.contrib import admin
from historiaclinica.models import HistoriaClinica

class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', )
    autocomplete_fields = ('paciente', 'medico',)

admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)
