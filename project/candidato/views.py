from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CandidatoForm,CandidatoPerfilForm
from django.contrib import messages
from .models import Candidato
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse


def candidato_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user.is_active:
            login(request,user)
def lista_de_candidatos(request):
    candidatos = Candidato.objects.all().order_by('-id')
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
    cadastrado = False
    if request.method == "POST":
        candidato_form        = CandidatoForm(data=request.POST)
        candidato_perfil_form = CandidatoPerfilForm(data=request.POST)

        if candidato_form.is_valid() and candidato_perfil_form.is_valid():
            user = candidato_form.save()
            user.set_password(user.password)
            user.save()
            
            candidato           = candidato_perfil_form.save(commit=False)
            candidato.user      = user
            import pdb; pdb.set_trace();
            candidato.user_id = candidato.user.id
            candidato.nome = request.POST.get('nome')
            candidato.pretensao_salarial = request.POST.get('pretensao_salarial')
            candidato.escolaridade  =  request.POST.get('escolaridade')
            candidato.save()
            #candidato ='user_id': 7, 'nome': 'aaaaaaaaaaaa', 'pretensao_salarial': 'De 1.000 a 2.000', 'escolaridade': 'Ensino médio'}
            cadastrado = True
        else:
            print(candidato_form.errors,candidato_perfil_form.errors)
    else:
        candidato_form          = CandidatoForm()
        candidato_perfil_form   = CandidatoPerfilForm()

    return render(request,"cadastro_candidato.html",{'candidato_form':candidato_form,
                                                'candidato_perfil_form':candidato_perfil_form,
                                                'cadastrado':cadastrado})
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
