from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def cadastro_empresa(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
	form = UserCreationForm()
	return render(request,"empresa/cadastro.html",{'form':form})

def login_empresa(request):
	return render(request,"empresa/login.html",{})
