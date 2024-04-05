from django.urls import path
from ReceitaApp import views

urlpatterns = [
         
    path('', views.index, name = 'index'),
        #caminho     view correspondente    nome da url
    path('receitas/', views.listar_receitas, name = 'receitas'),
                #numero da receita
    path('receita/<int:id>', views.detalhes_receita, name = 'receita')
]

#Para cada url do site, coloco uma linha nessa lista urlpatterns