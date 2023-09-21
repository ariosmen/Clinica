from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse
from historiaclinica.models import HistoriaClinica
from historiaclinica.forms import HistoriaClinicaForm, HistoriaClinicaFormEdit
from pacientes.models import Paciente
from medicos.models import Medico


def historiaclinica(request, hc):
    pac = Paciente.objects.get(id=hc)
    hc = HistoriaClinica.objects.all().filter(paciente_id = hc)
    return render(request, 'historiaclinica.html', {'hc': hc, 'paciente': pac})

def ingreso(request, hc):
    
    paciente = get_object_or_404(Paciente, id=hc)
    form = HistoriaClinicaForm(initial={'paciente': paciente})
    
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('historiaclinica', args=[hc]))
        else:
            return render(request, 'ingreso.html', {'form': form})
        
    return render(request, 'ingreso.html', {'form': form, 'paciente': paciente})

def editar_hc(request, hc, pac):

    paciente = get_object_or_404(Paciente, id=pac)
    historia = get_object_or_404(HistoriaClinica, id=hc)
    form = HistoriaClinicaFormEdit(initial={'medico': historia.medico, 'descripcion': historia.descripcion})
    
    if request.method == 'POST':
        form = HistoriaClinicaFormEdit(data=request.POST, instance=historia)
        if form.is_valid():
            form.save()
            return redirect(reverse('historiaclinica', args=[paciente.id]))
        else:
            return render(request, 'editar.html', {'form': form})
    
    return render(request, 'editar_hc.html', {'form': form, 'ing':historia, 'pac': paciente})  
    
def eliminar_hc(request, hc, pac):
    
    paciente = get_object_or_404(Paciente, id=pac)
    historia = get_object_or_404(HistoriaClinica, id=hc)
    historia.delete()
    
    return redirect(reverse('historiaclinica', args=[paciente.id]))
    
    
