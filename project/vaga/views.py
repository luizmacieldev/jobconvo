from django.shortcuts import render,get_object_or_404
from utils.choices import FAIXA_SALARIAL_CHOICES,ESCOLARIDADE_MINIMA_CHOICES
from .forms import VagaForm
from .models import Vaga
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastrar_vaga(request):
    form = VagaForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save() # salva as informações do formulário
        form = VagaForm()
    return render(request,"vaga/cadastro.html",{'form':form})

def lista_de_vagas(request):
    lista_de_vagas = Vaga.objects.all().order_by('-id')
    return render(request,"vaga/lista_de_vagas.html",{'lista_de_vagas':lista_de_vagas})

def vaga_detalhe(request,pk=None):
    vaga = get_object_or_404(Vaga,pk=pk)
    context = {'vaga':vaga}
    return render(request, "vaga/vaga_detalhe.html", context)
