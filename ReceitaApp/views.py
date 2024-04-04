from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
                   #requisitar

def listar_receitas(request):
    nome = 'Arthur'
    ingredientes = ['Farinha', 'Ovos', 'Manteiga', 'Leite']
    #dicionario que vai levar os dados para o template
    #chave : valor
    context = {
        'Endereço' : 'Av.Marechal Tito',
        'Bairro' : 'São Miguel Paulista',
        'Cidade' : 'São Paulo',
        'Estado' : 'SP',
        'Nome' : nome,
        'Ingredientes' : ingredientes
    }

    #qual template essa view vai retornar
    return render(request, 'receitas.html', context)