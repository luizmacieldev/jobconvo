from django import forms
from .models import Vaga


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ('empresa','nome_da_vaga','faixa_salarial','requisitos','escolaridade_minima')
