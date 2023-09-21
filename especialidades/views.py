from django.shortcuts import get_object_or_404, render, redirect
from especialidades.forms import EspecialidadForm
from especialidades.models import Especialidad
from medicos.models import Medico


# REGISTRAR
def especialidades(request):
    form = EspecialidadForm()
    medicos = Medico.objects.all()
    esp = Especialidad.objects.all()
        
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = EspecialidadForm()
            return redirect('especialidades')
            
        else:
            return render(request, 'especialidades.html', {'form': form})
        
    return render(request, 'especialidades.html', {'form': form, 'esp': esp, 'medicos': medicos})

# ELIMINAR
def eliminar_especialidad(request, esp):
    
    eliminar_especialidad = Especialidad.objects.get(id=esp)
    eliminar_especialidad.delete()

    return redirect('especialidades')
    
# EDITAR
def editar_especialidad(request, especialidad):
    
    editar_especialidad = get_object_or_404(Especialidad, id = especialidad)
    esp = EspecialidadForm()
    
    if request.method == 'POST':
        esp = EspecialidadForm(data=request.POST, instance=especialidad)
        if esp.is_valid():
            esp.save()
            esp = EspecialidadForm()
            return redirect('especialidades')
        else:
            return render(request, 'especialidades', {'esp': esp})
    
    return render(request, 'especialidades', {'esp': esp})

