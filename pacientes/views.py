from django.shortcuts import get_object_or_404, render, redirect
from pacientes.forms import PacienteForm
from pacientes.models import Paciente
from turnos.models import Turno


#LISTAR
def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})

# REGISTRAR
def registrar_paciente(request):
    valid = False
    form = PacienteForm()
    pacientes = Paciente.objects.all()
    
    if request.method == 'POST':
        form = PacienteForm(data=request.POST)
        if form.is_valid():
            valid = True
            form.save()
            form = PacienteForm()
            return render(request, 'pacientes.html', {'valid': valid, 'pacientes': pacientes})
        else:
            return render(request, 'registrar_paciente.html', {'form': form, 'valid': valid})
        
    return render(request, 'registrar_paciente.html', {'form': form, 'pacientes': pacientes, 'valid': valid})

# ELIMINAR
def eliminar_paciente(request, paciente):
    
    eliminar_paciente = Paciente.objects.get(id=paciente)
    eliminar_paciente.delete()
    
    return redirect('pacientes')

# EDITAR
def editar_paciente(request, paciente):

    turnos = Turno.objects.all().filter(paciente_id=paciente)
    valid = False
    pac = get_object_or_404(Paciente, id=paciente)
    
    fe = pac.fecha_nacimiento
    if fe.day >= 1 and fe.day <= 9:
        day = '0' + str(fe.day)
    else:
        day = str(fe.day)
    if fe.month >= 1 and fe.month <= 9:
        month = '0' + str(fe.month)
    else:
        month = str(fe.month)
        
    fecha = str(fe.year)+ "-" + month + "-" + day
    
    pac.fecha_nacimiento = fecha
    
    form = PacienteForm(instance=pac)
    
    if request.method == 'POST':
        form = PacienteForm(data=request.POST, instance=pac)
        if form.is_valid():
            valid = True
            form.save()
            form = PacienteForm()
            return redirect('pacientes')
        else:
            return render(request, 'editar_paciente.html', {'form': form})
    
    return render(request, 'editar_paciente.html', {'form': form, 'valid' : valid, 'paciente': pac, 'turnos': turnos})    

# BUSQUEDA
def busqueda(request):
    valid = False
    dni = request.POST['buscador']
    pacientes = Paciente.objects.all()
    
    try:
        paciente = Paciente.objects.get(dni = dni)
        
        fe = paciente.fecha_nacimiento
        if fe.day >= 1 and fe.day <= 9:
            day = '0' + str(fe.day)
        else:
            day = str(fe.day)
        if fe.month >= 1 and fe.month <= 9:
            month = '0' + str(fe.month)
        else:
            month = str(fe.month)
            
        fecha = str(fe.year)+ "-" + month + "-" + day
        
        paciente.fecha_nacimiento = fecha

        form = PacienteForm(instance=paciente)
        if request.method == 'POST':
            form = PacienteForm(instance=paciente)
            if form.is_valid():
                valid = True
                form.save()
                form = PacienteForm()
                return redirect('busqueda')
            else:
                return render(request, 'busqueda.html', {'form': form, 'valid': valid, 'paciente': paciente})
        
    except Paciente.DoesNotExist:
        return render(request, 'pacientes.html', {'pacientes': pacientes})

    # return render(request, 'busqueda.html', {'form':form, 'paciente': paciente})

