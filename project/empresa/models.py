from django.db import models
from django.conf import settings

# Create your models here.


class Perfil(models.Model):
	user 	= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	perfil  = models.CharField(max_length=200,choices=((1,'empresa'),(2,'candidato')))


	def __str__(self):
		return self.user.username
