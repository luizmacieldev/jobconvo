from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.relatorio,name='relatorio'),
]
    
