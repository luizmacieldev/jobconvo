from django.shortcuts import render
from utils.choices import FAIXA_SALARIAL_CHOICES,ESCOLARIDADE_MINIMA_CHOICES
from .forms import VagaForm
# Create your views here.
def cadastrar_vaga(request):
    form = VagaForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save() # salva as informações do formulário
        form = VagaForm()
    return render(request,"vaga/cadastro.html",{'form':form})
