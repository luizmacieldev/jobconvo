from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import EmpresaForm,EmpresaPerfilForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def cadastro_empresa(request):
	cadastrado = False
	if request.method == "POST":
		empresa_form 		 = EmpresaForm(data=request.POST)
		empresa_perfil_form  = EmpresaPerfilForm(data=request.POST)
		if empresa_form.is_valid() and empresa_perfil_form.is_valid():
			user = empresa_form.save()
			user.is_staff = True
			user.set_password(user.password)
			user.save()

			empresa = empresa_perfil_form.save(commit=False)
			empresa.user = user

			empresa.user_id = empresa.user.id
			empresa.nome	= request.POST.get('nome')
			empresa.save()

			cadastrado = True
		else:
			print(empresa_form.errors,candidato_perfil_form.errors)
	else:
		empresa_form = EmpresaForm()
		empresa_perfil_form = EmpresaPerfilForm()

	return render(request,"empresa/cadastro.html",{'empresa_form':empresa_form,
													'empresa_perfil_form':empresa_perfil_form,
													'cadastrado':cadastrado
												})

def login_empresa(request):
	return render(request,"empresa/login.html",{})
