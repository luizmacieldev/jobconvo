from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CandidatoForm
from django.contrib import messages
from .models import Candidatado
# Create your views here.

def lista_de_candidatos(request):
    candidatos = Candidatado.objects.all().order_by('-id')
    #queryset = request.GET.get('q')

    # if queryset:
    #     clientes = Cliente.objects.filter(
    #         Q(nome__icontains=queryset)|
    #         Q(email__icontains=queryset)| # LIKE % ana %
    #         Q(cpf__icontains=queryset)
    #     )
    # paginator = Paginator(clientes, 5) 
    # page = request.GET.get('page')
    # clientes = paginator.get_page(page)

    return render(request,"candidato/lista_de_candidatos.html",{'candidatos':candidatos})

def cadastro_candidato(request):
	form = CandidatoForm(request.POST)
	if form.is_valid():
		obj = form.save()
		obj.save()
		form = CandidatoForm()
		messages.success(request,"Candidato adicionado com sucesso")
		return redirect('home')

	return render(request,"candidato/index.html",{'form':form})
'''
def adicionar_cliente(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ClienteForm()
        messages.success(request,"Cliente adicionado com sucesso")
        return redirect('lista_de_clientes')
    return render(request,"clientes/adicionar_cliente.html",{'form':form})
	'''
