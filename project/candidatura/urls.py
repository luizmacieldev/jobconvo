from django.urls import path
from . import views 



urlpatterns = [
	path('',views.candidatura_vaga,name='candidatura_vaga')
]