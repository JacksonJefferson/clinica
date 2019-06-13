from django.shortcuts import render
from . models import Paciente, Medico, Medicamento

def home(request):
    return render (request, 'home.html')

def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render (request, 'paciente/list.html', {'pacientes': pacientes})

def paciente_show(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    return render (request, 'paciente/show.html', {'paciente': paciente})

def medico_list(request):
    medicos = Medico.objects.all()
    return render (request, 'medico/list.html', {'medicos': medicos})

def medico_show(request, medico_id):
    medico = Medico.objects.get(id=medico_id)
    return render (request, 'medico/show.html', {'medico': medico})
    

def agendamento_list(request):
    
    return render (request, 'agendamento/list.html')

def medicamento_list(request):
    medicamentos = Medicamento.objects.all()
    return render (request, 'medicamento/list.html', {'medicamentos': medicamentos})