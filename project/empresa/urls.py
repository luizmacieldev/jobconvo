from django.urls import path
from . import views 

app_name='empresa'

urlpatterns = [
	path('cadastro/',views.cadastro_empresa,name='cadastro_empresa'),
	path('login_empresa/',views.login_empresa,name='login_empresa'),
	path('logout_empresa/',views.logout_empresa,name='logout_empresa')
]