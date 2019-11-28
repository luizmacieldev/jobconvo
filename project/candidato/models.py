from django.db import models
from utils.choices import FAIXA_SALARIAL_CHOICES,ESCOLARIDADE_MINIMA_CHOICES
from django.contrib.auth.models import User

class Candidato(models.Model):
	user 				= models.OneToOneField(User,on_delete=models.CASCADE)
	nome				= models.CharField(max_length=200)
	pretensao_salarial  = models.CharField(max_length=25,choices=FAIXA_SALARIAL_CHOICES)
	escolaridade        = models.CharField(max_length=25,choices=ESCOLARIDADE_MINIMA_CHOICES)
    
	def __str__(self):
		return self.user.email