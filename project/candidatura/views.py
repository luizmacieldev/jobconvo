from django.shortcuts import render
from .forms import CandidaturaForm
# Create your views here.
from .models import Candidatura


def candidatura_vaga(request):
    form = CandidaturaForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save() # salva as informações do formulário
        objeto.candidato = request.user
        form = CandidaturaForm()
    return render(request,"candidatura/cadastro.html",{'form':form})