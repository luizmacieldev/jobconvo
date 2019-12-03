from django import forms
from .models import Empresa
from django.contrib.auth import get_user_model

User = get_user_model()


class EmpresaForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model 	= User
		fields 	= ('email','password')
	
	def save(self, commit=True):
		user = super(EmpresaForm,self).save(commit = False)
		user.username = user.email
		if commit:
			user.save()
		return user
	
class EmpresaPerfilForm(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = ('nome',)