from django.shortcuts import render
from ReceitaApp.models import Receita, Categoria
# Create your views here.

def index(request):

    categorias = Categoria.objects.all()
    context = {
        'categorias' : categorias
    }

    return render(request, 'index.html', context)
                   #requisitar
        

def listar_receitas(request):
    #Buscar as receitas no banco de dados utilizando ORM do Django

    #ta puxando tudo la do banco de dados
    receitas = Receita.objects.all()

    
    #dicionario que vai levar os dados para o template
    #chave : valor
    context = {
        'receitas' : receitas
    }
    
    #qual template essa view vai retornar
    return render(request, 'receitas.html ', context)

def detalhes_receita(request, id):
    #vamo aqui buscar a receita referente a seu id
    receita = Receita.objects.get(id = id)

    context = {
        'receita' : receita
    }    
    
    return render(request, 'receita.html', context)