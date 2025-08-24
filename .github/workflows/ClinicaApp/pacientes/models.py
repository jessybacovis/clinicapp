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
