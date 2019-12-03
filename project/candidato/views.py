from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CandidatoForm,CandidatoPerfilForm
from django.contrib import messages
from .models import Candidato
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages


def login_candidato(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request,'Usuario logado com sucesso')
                return HttpResponseRedirect(reverse('pagina_inicial'))
        else:
            return HttpResponse('Erro usuário ou senha inválido')
    return render(request,"login_candidato.html",{})


@login_required
def logout_candidato(request):
    logout(request)
    return HttpResponseRedirect(reverse('pagina_inicial'))


def lista_de_candidatos(request):
    candidatos = Candidato.objects.all().order_by('-id')
    return render(request,"candidato/lista_de_candidatos.html",{'candidatos':candidatos})

def cadastro_candidato(request):
    cadastrado = False
    if request.method == "POST":
        candidato_form        = CandidatoForm(data=request.POST)
        candidato_perfil_form = CandidatoPerfilForm(data=request.POST)

        if candidato_form.is_valid() and candidato_perfil_form.is_valid():
            user = candidato_form.save()
            user.is_candidato = True
            user.set_password(user.password)
            user.save()
            candidato           = candidato_perfil_form.save(commit=False)
            candidato.user      = user
            candidato.user_id = candidato.user.id
            candidato.nome = request.POST.get('nome')
            candidato.pretensao_salarial = request.POST.get('pretensao_salarial')
            candidato.escolaridade  =  request.POST.get('escolaridade')
            candidato.save()
            cadastrado = True
            messages.success(request,'Candidato cadastrado com sucesso, por favor faça o login')
            return HttpResponseRedirect(reverse('candidato:login_candidato'))
        else:
            print(candidato_form.errors,candidato_perfil_form.errors)
    else:
        candidato_form          = CandidatoForm()
        candidato_perfil_form   = CandidatoPerfilForm()

    return render(request,"cadastro_candidato.html",{'candidato_form':candidato_form,
                                                'candidato_perfil_form':candidato_perfil_form,
                                                'cadastrado':cadastrado})
