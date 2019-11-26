from django.contrib import admin
from .models import Candidatura
# Register your models here.
from .models import Vaga

class VagaAdmin(admin.ModelAdmin):
    list_display = ('nome_da_vaga','faixa_salarial','escolaridade_minima')
    class Meta:
        model = Vaga 

admin.site.register(Vaga,VagaAdmin)
admin.site.register(Candidatura)