from django.db import models
from utils.choices import FAIXA_SALARIAL_CHOICES,ESCOLARIDADE_MINIMA_CHOICES
from usuario.models import User
from datetime import datetime

class Candidato(models.Model):
	user             	= models.ForeignKey(User,on_delete=models.DO_NOTHING)
	nome				= models.CharField(max_length=200)
	pretensao_salarial  = models.CharField(max_length=25,choices=FAIXA_SALARIAL_CHOICES)
	escolaridade        = models.CharField(max_length=25,choices=ESCOLARIDADE_MINIMA_CHOICES)
	criado_em			= models.PositiveSmallIntegerField(default=datetime.now().month)
	
	def __str__(self):
		return self.nome

