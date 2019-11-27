from django.urls import path
from . import views 



urlpatterns = [
	path('',views.lista_de_candidatos,name="lista_de_candidatos"),
	path('cadastro/',views.cadastro_candidato,name='cadastro_candidato')

]