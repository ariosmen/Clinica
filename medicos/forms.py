from django import forms
from medicos.models import Medico
from django.contrib.admin.widgets import AdminDateWidget

class MedicoForm(forms.ModelForm):
    
    class Meta:
        model = Medico
        # fields = '__all__' #ESTO AGREGA TODOS LOS CAMPOS EN EL ORDEN DEL MODELS
        fields = ['nombre', 'apellido', 'dni', 'direccion', 'telefono', 'email', 'estado_civil', 'fecha_nacimiento', 'especialidad', 'sexo']
        widgets = {
            'fecha_nacimiento' : AdminDateWidget(
                attrs={
                    'style': 'font-size: 13px',
                    'type': 'date',
                }
            ),
            'nombre' : forms.DateInput(
                attrs={
                    'autofocus' : True,
                }
            ),
        }
        
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].capitalize()
        return nombre
        
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido'].capitalize()
        return apellido
        
    def clean_direccion(self):
        direccion = self.cleaned_data['direccion'].capitalize()
        return direccion
        
class MedicoFormEdit(forms.ModelForm):
    
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Medico
        # fields = '__all__' #ESTO AGREGA TODOS LOS CAMPOS EN EL ORDEN DEL MODELS
        fields = ['nombre', 'apellido', 'dni', 'direccion', 'telefono', 'email', 'estado_civil', 'fecha_nacimiento', 'especialidad','sexo', 'activo']
        widgets = {
            'nombre' : forms.DateInput(
                attrs={
                    'autofocus' : True,
                }
            ),
        }
        
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].capitalize()
        return nombre
        
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido'].capitalize()
        return apellido

    def clean_direccion(self):
        direccion = self.cleaned_data['direccion'].capitalize()
        return direccion

