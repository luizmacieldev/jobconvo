from django.urls import path
from . import views 



urlpatterns = [
	path('',views.login_candidato,name='login_candidato')
]