from django.db import models
from candidato.models import Candidato
from empresa.models import Empresa
from utils.choices import FAIXA_SALARIAL_CHOICES,ESCOLARIDADE_MINIMA_CHOICES


class Vaga(models.Model):
    empresa                 = models.ForeignKey('empresa.Empresa',on_delete=models.CASCADE)
    nome_da_vaga            = models.CharField(max_length=255)
    faixa_salarial          = models.CharField(max_length=100,choices=FAIXA_SALARIAL_CHOICES)
    requisitos              = models.TextField()
    escolaridade_minima     = models.CharField(max_length=200,choices=ESCOLARIDADE_MINIMA_CHOICES)

    def __str__(self):
        return self.nome_da_vaga






    