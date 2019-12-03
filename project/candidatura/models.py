from django.db import models
from vaga.models import Vaga
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# Create your models here.


class Candidatura(models.Model):
    vaga = models.ForeignKey('vaga.Vaga',on_delete=models.CASCADE)
    candidato = models.OneToOneField('candidato.Candidato',on_delete=models.CASCADE)


    def __str__(self):
        return 'Vaga {} , candidato {}'.format(self.vaga.nome_da_vaga,self.candidato.nome)

    class Meta:
        unique_together = ('vaga','candidato')

    def validate_unique(self,exclude=None):
        try:
            super(Candidatura,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Erro, você já se candidatou a essa vaga")

    @property
    def bonus(self):
        pontos = 0
        if self.candidato.pretensao_salarial == self.vaga.faixa_salarial:
            pontos = pontos + 1
        if self.candidato.escolaridade == self.vaga.escolaridade_minima:
            pontos = pontos + 1
        return pontos


    