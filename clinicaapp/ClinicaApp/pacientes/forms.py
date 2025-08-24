from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'telefone', 'email', 'historico']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
        Agendamento
        from django import forms
from .models import Paciente, Agendamento

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'telefone', 'email', 'historico']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['paciente', 'data_hora', 'observacoes']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        