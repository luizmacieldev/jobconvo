from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import EmpresaForm
from django.contrib import messages
# Create your views here.
def cadastro_empresa(request):
	form = EmpresaForm(request.POST)
	if form.is_valid():
		obj = form.save()
		obj.save()
		form = EmpresaForm()
		messages.success(request,"Empresa adicionado com sucesso")
		return redirect('home')

	return render(request,"empresa/cadastro.html",{'form':form})

def login_empresa(request):
	return render(request,"empresa/login.html",{})
