from django.urls import path
from . import views 



urlpatterns = [
	path('cadastro/',views.cadastrar_vaga,name='cadastrar_vaga'),
	path('lista_de_vagas/',views.lista_de_vagas,name='lista_de_vagas'),
	path('lista_de_vagas/<int:pk>/',views.vaga_detalhe,name='vaga_detalhe')

]