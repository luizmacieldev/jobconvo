from django.shortcuts import render
from vaga.models import Vaga
from candidato.models import Candidato
from datetime import datetime

def relatorio(request):
	mes_atual = datetime.now().month
	vaga = Vaga.objects.filter(criado_em=mes_atual).count()
	candidato = Candidato.objects.filter(criado_em=mes_atual).count()
	return render(request,"relatorio/index.html",{'vaga':vaga,'candidato':candidato})