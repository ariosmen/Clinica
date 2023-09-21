from django import forms
from turnos.models import Turno

class TurnoForm(forms.ModelForm):
    
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Turno
        fields = ['fecha', 'hora', 'medico', 'especialidad', 'paciente']