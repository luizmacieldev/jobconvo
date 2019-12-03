from django.db import models
from usuario.models import User


class Empresa(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	nome	= models.CharField(max_length=200)

	def __str__(self):
		return self.nome
	