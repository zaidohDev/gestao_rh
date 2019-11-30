from django.db import models


# Create your models here.
class Documento(models.Model):
    nome = models.CharField(max_length=100, help_text="Documentos")

    def __str__(self):
        return self.nome