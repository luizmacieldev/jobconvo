from django import forms
from .models import Candidatado

class CandidatoForm(forms.ModelForm):
	class Meta:
		model 	= Candidatado
		fields 	= ('nome','pretensao_salarial','ultima_escolaridade')
	
		