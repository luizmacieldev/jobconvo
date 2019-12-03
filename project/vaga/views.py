from django.shortcuts import render,get_object_or_404,reverse,redirect
from utils.choices import FAIXA_SALARIAL_CHOICES,ESCOLARIDADE_MINIMA_CHOICES
from .forms import VagaForm
from .models import Vaga
from candidatura.models import Candidatura
from candidato.models import Candidato
from django.contrib.auth.decorators import login_required
from .models import Empresa
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

@login_required
def cadastrar_vaga(request):
    if request.user.is_empresa:
        form = VagaForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.save() # salva as informações do formulário
            form = VagaForm()
            messages.success(request,"Vaga cadastrada com sucesso")
            return HttpResponseRedirect(reverse('pagina_inicial'))
        return render(request,"vaga/cadastro.html",{'form':form})

@login_required
def lista_de_vagas(request):
    lista_de_vagas = Vaga.objects.all().order_by('-id')
    return render(request,"vaga/lista_de_vagas.html",{'lista_de_vagas':lista_de_vagas})

@login_required
def vaga_detalhe(request,pk=None):
    vaga = get_object_or_404(Vaga,pk=pk)
    context = {'vaga':vaga}
    return render(request, "vaga/vaga_detalhe.html", context)

@login_required
def editar_vaga(request,pk=None):
    vaga = get_object_or_404(Vaga,pk=pk)
    form = VagaForm(request.POST or None,instance=vaga)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request,"Vaga editada com sucesso")
        return redirect('vaga:lista_de_vagas')
    return render(request,"vaga/editar_vaga.html",{'form':form})

@login_required
def excluir_vaga(request,pk=None):
    vaga = get_object_or_404(Vaga,pk=pk)
    if request.method == "POST":
        vaga.delete()
        messages.warning(request,"Vaga Excluida com sucesso")
        return redirect('vaga:lista_de_vagas')
    return render(request,"vaga/excluir_vaga.html",{'vaga':vaga})

