from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('novo/', views.novo_paciente, name='novo_paciente'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('novo/', views.novo_paciente, name='novo_paciente'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('novo/', views.novo_paciente, name='novo_paciente'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', views.novo_agendamento, name='novo_agendamento'),
]
<int:pk>
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('novo/', views.novo_paciente, name='novo_paciente'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', views.novo_agendamento, name='novo_agendamento'),
    path('agendamentos/editar/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamentos/excluir/<int:pk>/', views.excluir_agendamento, name='excluir_agendamento'),
]
from django.urls import path
from . import views

urlpatterns = [
    # ... (rotas existentes) ...
    path('financeiro/', views.lista_transacoes, name='lista_transacoes'),
    path('financeiro/novo/', views.nova_transacao, name='nova_transacao'),
]
from django.contrib import admin
from django.urls import path, include
from pacientes.views import home # Importamos a view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('pacientes/', include('pacientes.urls')),
]
