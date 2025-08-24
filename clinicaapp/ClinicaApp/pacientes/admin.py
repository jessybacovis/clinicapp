from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'email')
    list_filter = ('data_nascimento',)
    Agendamento
    from django.contrib import admin
from .models import Paciente, Agendamento # Importamos o novo modelo

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'email')
    list_filter = ('data_nascimento',)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data_hora', 'observacoes')
    search_fields = ('paciente__nome', 'observacoes')
    list_filter = ('data_hora',)
    from django.contrib import admin
from .models import Paciente, Agendamento, Transacao # Importamos o novo modelo

# ... (código dos registros existentes) ...

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'descricao', 'valor', 'data')
    list_filter = ('data',)
    search_fields = ('paciente__nome', 'descricao')
    