from django.shortcuts import render
from .models import Paciente

def lista_pacientes(request):
    """
    View para listar todos os pacientes.
    """
    pacientes = Paciente.objects.all().order_by('nome')
    context = {'pacientes': pacientes}
    return render(request, 'pacientes/lista_pacientes.html', context)

def novo_paciente(request):
    """
    View para adicionar um novo paciente (por enquanto, apenas uma página placeholder).
    """
    return render(request, 'pacientes/novo_paciente.html')
  
