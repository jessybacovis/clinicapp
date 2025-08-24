from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm  # Importamos o formulário

def lista_pacientes(request):
    """
    View para listar todos os pacientes.
    """
    pacientes = Paciente.objects.all().order_by('nome')
    context = {'pacientes': pacientes}
    return render(request, 'pacientes/lista_pacientes.html', context)

def novo_paciente(request):
    """
    View para adicionar um novo paciente.
    """
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')  # Redireciona para a lista
    else:
        form = PacienteForm()
    
    return render(request, 'pacientes/novo_paciente.html', {'form': form})
