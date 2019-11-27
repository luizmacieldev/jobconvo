from django.db import models
from django.contrib.auth.models import AbstractUser

FAIXA_SALARIAL_CHOICES = (
    ('Até 1.000','Até 1.000'),
    ('De 1.000 a 2.000','De 1.000 a 2.000'),
    ('De 2.000 a 3.000','De 2.000 a 3.000'),
    ('Acima de 3.000','Acima de 3.000'),
)

ESCOLARIDADE_MINIMA_CHOICES = (
    ('Ensino fundamental','Ensino fundamental'),
    ('Ensino médio','Ensino médio'),
    ('Tecnólogo','Tecnólogo'),
    ('Ensino Superior','Ensino Superior'),
    ('Pós / MBA / Mestrado','Pós / MBA / Mestrado'),
    ('Doutorado','Doutorado')
)
class Candidatado(models.Model):
    nome = models.CharField(max_length=200)
    pretensao_salarial = models.CharField(max_length=200,choices=FAIXA_SALARIAL_CHOICES)
    ultima_escolaridade = models.CharField(max_length=200,choices=ESCOLARIDADE_MINIMA_CHOICES)



    def __str__(self):
        return self.nome