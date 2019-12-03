from django.urls import path
from . import views 

app_name='candidatura'

urlpatterns = [
	path('candidatar_vaga/<int:pk>/',views.candidatar_vaga,name='candidatar_vaga'),
	path('listar_candidaturas/',views.listar_candidaturas,name='listar_candidaturas')
]