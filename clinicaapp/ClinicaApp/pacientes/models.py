from django.db import models

class Paciente(models.Model):
    """
    Modelo para armazenar as informações dos pacientes.
    """
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    historico = models.TextField(blank=True)

    def __str__(self):
        """
        Retorna o nome do paciente quando o objeto é chamado.
        """
        return self.nome
    from django.db import models

class Paciente(models.Model):
    # ... (código existente do modelo Paciente) ...

class Agendamento(models.Model):
    """
    Modelo para armazenar os agendamentos de consultas.
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='agendamentos')
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        """
        Retorna uma representação do agendamento.
        """
        return f'Consulta de {self.paciente.nome} em {self.data_hora.strftime("%d/%m/%Y às %H:%M")}'
    from django.db import models
from django.db.models import Sum

class Paciente(models.Model):
    # ... (código existente do modelo Paciente) ...

class Agendamento(models.Model):
    # ... (código existente do modelo Agendamento) ...

class Transacao(models.Model):
    """
    Modelo para registrar as transações financeiras.
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='transacoes')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        """
        Retorna uma representação da transação.
        """
        return f'{self.descricao} de {self.paciente.nome} - R$ {self.valor}'
    