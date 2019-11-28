from django.db import models
from django.conf import settings


class Empresa(models.Model):
	nome	= models.CharField(max_length=200)

	def __str__(self):
		return self.nome
	