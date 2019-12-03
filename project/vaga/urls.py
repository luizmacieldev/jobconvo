from django.urls import path,include
from . import views 

app_name = 'vaga'

urlpatterns = [
	path('cadastro_de_vagas/',views.cadastrar_vaga,name='cadastrar_vaga'),
	path('lista_de_vagas/',views.lista_de_vagas,name='lista_de_vagas'),
	path('lista_de_vagas/<int:pk>/',views.vaga_detalhe,name='vaga_detalhe'),
	path('editar_vaga/<int:pk>/',views.editar_vaga,name='editar_vaga'),
	path('excluir_vaga/<int:pk>/',views.excluir_vaga,name='excluir_vaga'),
	path('vaga_detalhe/<int:pk>/',views.vaga_detalhe,name='vaga_detalhe'),
	

]