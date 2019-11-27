from django.db import models
from candidato.models import Candidatado
from django.core.exceptions import ValidationError
# Create your models here.
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
class Vaga(models.Model):
    nome_da_vaga            = models.CharField(max_length=255)
    faixa_salarial          = models.CharField(max_length=100,choices=FAIXA_SALARIAL_CHOICES)
    requisitos              = models.TextField()
    escolaridade_minima     = models.CharField(max_length=200,choices=ESCOLARIDADE_MINIMA_CHOICES)

    def __str__(self):
        return self.nome_da_vaga


class Candidatura(models.Model):
    vaga = models.ForeignKey('Vaga',on_delete=models.CASCADE)
    candidato = models.ForeignKey('candidato.Candidatado',on_delete=models.CASCADE)


    class Meta:
        unique_together = ('vaga','candidato')

    def validate_unique(self,exclude=None):
        try:
            super(Candidatura,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Erro, você já se candidatou a essa vaga")


    