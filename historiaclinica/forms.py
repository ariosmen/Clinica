from django import forms
from historiaclinica.models import HistoriaClinica

class HistoriaClinicaForm(forms.ModelForm):
    
    class Meta:
        
        model = HistoriaClinica
        fields = ['paciente', 'medico', 'descripcion']


class HistoriaClinicaFormEdit(forms.ModelForm):
    
    class Meta:
        
        model = HistoriaClinica
        fields = ['medico', 'descripcion']
