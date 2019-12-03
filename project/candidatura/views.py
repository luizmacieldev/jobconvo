from django.shortcuts import render,get_object_or_404
from .forms import CandidaturaForm
# Create your views here.
from .models import Candidatura
from candidato.models import Candidato
from vaga.models import Vaga
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect



def listar_candidaturas(request):
	candidaturas = Candidatura.objects.all()
	return render(request,"candidatura/lista_de_candidaturas.html",{'candidaturas':candidaturas})

@login_required
def candidatar_vaga(request,pk=None):
    candidato = Candidato.objects.get(user=request.user)
    vaga = get_object_or_404(Vaga,pk=pk)
    candidatura = Candidatura.objects.create(candidato=candidato,vaga=vaga)
    candidatura.save()
    if candidatura:
        messages.success(request,"Inscrição realizado com sucesso.")
        return HttpResponseRedirect(reverse('pagina_inicial'))
    else:
        return HttpResponse('Houve um erro na Inscrição')