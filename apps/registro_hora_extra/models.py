from django.db import models
from apps.funcionarios.models import Funcionario


# Create your models here.
class RegistroHoraExtra(models.Model):
    nome = models.CharField(max_length=100, help_text="Registro de Hora Extra")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
