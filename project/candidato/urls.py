from django.urls import path,include
from . import views 

app_name='candidato'

urlpatterns = [
	path('',views.lista_de_candidatos,name="lista_de_candidatos"),
	path('cadastro/',views.cadastro_candidato,name='cadastro_candidato'),
	path('login_candidato/',views.login_candidato,name='login_candidato'),
	path('logout_candidato/',views.logout_candidato,name='logout_candidato')

]