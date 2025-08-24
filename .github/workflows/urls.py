from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('novo/', views.novo_paciente, name='novo_paciente'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('novo/', views.novo_paciente, name='novo_paciente'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
]
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
