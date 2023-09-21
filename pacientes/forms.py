from django import forms
from pacientes.models import Paciente

class PacienteForm(forms.ModelForm):
     
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
                
        model = Paciente
        # fields = '__all__' #ESTO AGREGA TODOS LOS CAMPOS EN EL ORDEN DEL MODELS
        fields = ['activo', 'nombre', 'apellido', 'dni', 'sexo', 'direccion', 'telefono', 'email', 'estado_civil', 'fecha_nacimiento', 'obra_social']
        # labels = {'fecha_nacimiento': '.',} #ESTO LO HACE POR DEFECTO
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
        
# class PacienteFormEdit(forms.ModelForm):
    
    
#     class Meta:
                
#         model = Paciente
#         # fields = '__all__' #ESTO AGREGA TODOS LOS CAMPOS EN EL ORDEN DEL MODELS
#         fields = ['nombre', 'apellido', 'dni', 'sexo', 'direccion', 'telefono', 'email', 'estado_civil', 'fecha_nacimiento', 'obra_social', 'activo']
#         # labels = {'fecha_nacimiento': '.',} #ESTO LO HACE POR DEFECTO
#         widgets = {
#             'nombre' : forms.DateInput(
#                 attrs={
#                     'autofocus' : True,
#                 }
#             ),
#         }
        
#     def clean_nombre(self):
#         nombre = self.cleaned_data['nombre'].capitalize()
#         return nombre
        
#     def clean_apellido(self):
#         apellido = self.cleaned_data['apellido'].capitalize()
#         return apellido

#     def clean_direccion(self):
#         direccion = self.cleaned_data['direccion'].capitalize()
#         return direccion