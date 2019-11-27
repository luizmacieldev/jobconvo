from djngo import forms
from .models import Candidato

class CandidatoForm(forms.ModelForm):
	class Meta:
		model 	= Candidato
		fields 	= ('nome',,'pretensao_salarial','ultima_escolaridade')
	
		