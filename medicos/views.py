from django.shortcuts import get_object_or_404, render, redirect
from medicos.forms import MedicoForm, MedicoFormEdit
from medicos.models import Medico
from especialidades.forms import EspecialidadForm, Especialidad


def medicos(request):
    medicos = Medico.objects.all()
    
    return render(request, 'medicos.html', {'medicos': medicos})

# REGISTRAR
def registrar_medico(request):
    valid = False
    
    form = MedicoForm()
    esp = EspecialidadForm()
    espe = Especialidad.objects.all()
    
    if request.method == 'POST':
        form = MedicoForm(data=request.POST)
        esp = EspecialidadForm(request.POST)
        
        if form.is_valid():
            valid = True
            form.save()
            form = MedicoForm()
            esp = EspecialidadForm()
            return redirect('registrar_medico')
        
        elif esp.is_valid():
            esp.save()
            form = MedicoForm()
            esp = EspecialidadForm()
            return redirect('registrar_medico')
        
        else:
            return render(request, 'registrar_medico.html', {'form': form, 'valid': valid, 'esp': esp, 'medicos': medicos})
        
    return render(request, 'registrar_medico.html', {'form': form, 'esp': esp, 'medicos': medicos, 'espe': espe})

# ELIMINAR
def eliminar_medico(request, medico):
    
    eliminar_medico = Medico.objects.get(id=medico)
    eliminar_medico.delete()
    
    return redirect('registro_medico')

# EDITAR
def editar_medico(request, medico):
    
    valid = False
    editar_medico = get_object_or_404(Medico, id=medico)
    
    fe = editar_medico.fecha_nacimiento
    if fe.day >= 1 and fe.day <= 9:
        day = '0' + str(fe.day)
    else:
        day = str(fe.day)
    if fe.month >= 1 and fe.month <= 9:
        month = '0' + str(fe.month)
    else:
        month = str(fe.month)
        
    fecha = str(fe.year)+ "-" + month + "-" + day
    
    editar_medico.fecha_nacimiento = fecha
    
    form = MedicoFormEdit(instance=editar_medico)
    esp = EspecialidadForm()
    
    print(editar_medico)
    
    if request.method == 'POST':
        form = MedicoFormEdit(data=request.POST, instance=editar_medico)
        if form.is_valid():
            valid = True
            form.save()
            form = MedicoFormEdit()
            esp = EspecialidadForm()
            return redirect('medicos')
        else:
            return render(request, 'editar_medico.html', {'form': form, 'esp': esp})
    
    return render(request, 'editar_medico.html', {'form': form, 'esp': esp, 'medico': editar_medico, 'valid' : valid})
