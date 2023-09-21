from django import forms
from especialidades.models import Especialidad

class EspecialidadForm(forms.ModelForm):
    
    class Meta:
        model = Especialidad
        fields = ['especialidad', ]
        widgets = {
            'especialidad': forms.DateInput(
                attrs={
                    'autofocus': True,
                }
            )            
        }

    def clean_especialidad(self):
        especialidad = self.cleaned_data['especialidad'].capitalize()
        return especialidad

