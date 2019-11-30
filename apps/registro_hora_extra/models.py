from django.db import models


# Create your models here.
class RegistroHoraExtra(models.Model):
    nome = models.CharField(max_length=100, help_text="Registro de Hora Extra")

    def __str__(self):
        return self.nome
