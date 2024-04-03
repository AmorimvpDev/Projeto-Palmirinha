from django.contrib import admin

from ReceitaApp.models import Receita, Categoria
# Register your models here.
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'grau_de_dificuldade']

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Categoria)