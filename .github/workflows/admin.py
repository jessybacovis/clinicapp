from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'email')
    list_filter = ('data_nascimento',)
  
