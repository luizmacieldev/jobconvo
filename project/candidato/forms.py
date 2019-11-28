from django import forms
from django.contrib.auth.models import User
from .models import Candidato

class CandidatoForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model 	= User
		fields 	= ('email','password')

	def save(self,commit = True):
		user = super(CandidatoForm, self).save(commit = False)
		user.username = user.email
		if commit:
			user.save()
		return user

class CandidatoPerfilForm(forms.ModelForm):
	class Meta:
		model 	= Candidato
		fields 	= ('nome','pretensao_salarial','escolaridade')
	
