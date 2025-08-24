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
