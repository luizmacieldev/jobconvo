from django.db import models
from vaga.models import Vaga
from django.core.exceptions import ValidationError
# Create your models here.


class Candidatura(models.Model):
    vaga = models.ForeignKey('vaga.Vaga',on_delete=models.CASCADE)
    candidato = models.ForeignKey('candidato.Candidato',on_delete=models.CASCADE)


    class Meta:
        unique_together = ('vaga','candidato')

    def validate_unique(self,exclude=None):
        try:
            super(Candidatura,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Erro, você já se candidatou a essa vaga")
