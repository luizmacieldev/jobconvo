from django.shortcuts import render

# Create your views here.
def relatorio(request):
    return render(request,"relatorio/index.html",{})