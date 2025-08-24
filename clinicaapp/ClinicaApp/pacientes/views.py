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
novo_paciente
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
Agendamento
from django.shortcuts import render, redirect
from .models import Paciente, Agendamento  # Importamos o modelo Agendamento
from .forms import PacienteForm

# ... (código das views existentes) ...

def lista_agendamentos(request):
    """
    View para listar todos os agendamentos.
    """
    agendamentos = Agendamento.objects.all().order_by('data_hora')
    context = {'agendamentos': agendamentos}
    return render(request, 'pacientes/lista_agendamentos.html', context)
novo_agendamento
from django.shortcuts import render, redirect
from .models import Paciente, Agendamento
from .forms import PacienteForm, AgendamentoForm # Importamos o novo formulário

# ... (views existentes) ...

def novo_paciente(request):
    # ... (código existente) ...

def lista_agendamentos(request):
    # ... (código existente) ...

def novo_agendamento(request):
    """
    View para adicionar um novo agendamento.
    """
    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    
    return render(request, 'pacientes/novo_agendamento.html', {'form': form})
get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Agendamento
from .forms import PacienteForm, AgendamentoForm

# ... (views existentes) ...

def editar_agendamento(request, pk):
    """
    View para editar um agendamento existente.
    """
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == "POST":
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    
    return render(request, 'pacientes/editar_agendamento.html', {'form': form})

def excluir_agendamento(request, pk):
    """
    View para excluir um agendamento existente.
    """
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == "POST":
        agendamento.delete()
        return redirect('lista_agendamentos')
    
    return render(request, 'pacientes/confirmar_exclusao_agendamento.html', {'agendamento': agendamento})
lista_transacoes
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Agendamento, Transacao # Importamos Transacao
from .forms import PacienteForm, AgendamentoForm, TransacaoForm # Importamos o novo form
from django.db.models import Sum

# ... (views existentes) ...

def lista_transacoes(request):
    """
    View para listar todas as transações e calcular o total.
    """
    transacoes = Transacao.objects.all().order_by('-data')
    total_receita = transacoes.aggregate(Sum('valor'))['valor__sum'] or 0
    
    context = {
        'transacoes': transacoes,
        'total_receita': total_receita
    }
    return render(request, 'pacientes/lista_transacoes.html', context)

def nova_transacao(request):
    """
    View para adicionar uma nova transação.
    """
    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_transacoes')
    else:
        form = TransacaoForm()

    return render(request, 'pacientes/nova_transacao.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Agendamento, Transacao
from .forms import PacienteForm, AgendamentoForm, TransacaoForm
from django.db.models import Sum

def home(request):
    return render(request, 'pacientes/home.html')

# ... (restante das views) ...
