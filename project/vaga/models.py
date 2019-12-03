from django.db import models
from candidato.models import Candidato
from empresa.models import Empresa
from utils.choices import FAIXA_SALARIAL_CHOICES,ESCOLARIDADE_MINIMA_CHOICES
from datetime import datetime


class Vaga(models.Model):
    nome_da_vaga            = models.CharField(max_length=255)
    faixa_salarial          = models.CharField(max_length=100,choices=FAIXA_SALARIAL_CHOICES)
    requisitos              = models.TextField()
    escolaridade_minima     = models.CharField(max_length=200,choices=ESCOLARIDADE_MINIMA_CHOICES)
    criado_em				= models.PositiveSmallIntegerField(default=datetime.now().month)

    def __str__(self):
        return self.nome_da_vaga






    