from django.db import models
from django.contrib.auth.models import AbstractUser

PERFIL_CHOICES = (
	(1,'candidato'),
	(2,'empresa')
)
class CustomUser(AbstractUser):
    #perfil = models.PositiveSmallIntegerField(choices=PERFIL_CHOICES)

    def __str__(self):
        return self.email