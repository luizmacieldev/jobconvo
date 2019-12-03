from django import forms
from .models import Vaga
from empresa.models import Empresa
class VagaForm(forms.ModelForm):
	class Meta:
		model = Vaga
		fields = ('nome_da_vaga','faixa_salarial','requisitos','escolaridade_minima')
