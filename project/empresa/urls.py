from django.urls import path
from . import views 


urlpatterns = [
	path('cadastro/',views.cadastro_empresa,name='cadastro_empresa'),
	path('login/',views.login_empresa,name='login_empresa')
]