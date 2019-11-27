from django.shortcuts import render
from .forms import EmpresaForm
# Create your views here.
def cadastro_empresa(request):
	form = EmpresaForm()
	return render(request,"empresa/cadastro.html",{'form':form})

def login_empresa(request):
	return render(request,"empresa/login.html",{})
