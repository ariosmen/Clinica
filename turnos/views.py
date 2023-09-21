from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from pacientes.models import Paciente
from turnos.models import Turno
from turnos.forms import TurnoForm


def listar_turno(request):
    turnos = Turno.objects.all()
    return render(request, "turnos.html", {"turnos": turnos})

def registrar_turnos(request, pac):
    paciente = get_object_or_404(Paciente, id=pac)

    form = TurnoForm(initial={"paciente": paciente})

    if request.method == "POST":
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pacientes")
        else:
            return render(request, "turnos.html", {"form": form, "paciente": paciente})

    return render(request, "turnos.html", {"form": form, "paciente": paciente})

def editar_turnos(request, turno, paciente):
    pac = get_object_or_404(Paciente, id=paciente)
    turn = get_object_or_404(Turno, id=turno)

    fecha = turn.fecha
    if fecha.day >= 1 and fecha.day <= 9:
        day = "0" + str(fecha.day)
    else:
        day = str(fecha.day)
    if fecha.month >= 1 and fecha.month <= 9:
        month = "0" + str(fecha.month)
    else:
        month = str(fecha.month)
    
    turn.fecha = str(fecha.year) + "-" + month + "-" + day

    form = TurnoForm(instance=turn)

    if request.method == "POST":
        form = TurnoForm(data=request.POST, instance=turn)
        if form.is_valid():
            form.save()
            return redirect(reverse("editar_paciente", args=[pac.id]))
        else:
            return render(request, "editar_turno.html", {"form": form})

    return render(
        request, "editar_turno.html", {"form": form, "paciente": pac, "turno": turn}
    )

def eliminar_turnos(request, turno, paciente):
    pac = get_object_or_404(Paciente, id=paciente)
    tur = get_object_or_404(Turno, id=turno)
    tur.delete()

    return redirect(reverse("editar_paciente", args=[pac.id]))
