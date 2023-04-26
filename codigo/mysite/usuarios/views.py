from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa, Depoimento, Endereco
from .forms import PessoaForm, DepoimentoForm, EnderecoForm

# Views de Pessoa
def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'cadastrar_pessoa.html', {'form': form})

def editar_pessoa(request, id):
    pessoa = Pessoa.objects.get(pk=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'editar_pessoa.html', {'form': form})

def excluir_pessoa(request, id):
    pessoa = Pessoa.objects.get(pk=id)
    pessoa.delete()
    return redirect('lista_pessoas')

# Views de Depoimento
def criar_depoimento(request):
    if request.method == 'POST':
        form = DepoimentoForm(request.POST)
        if form.is_valid():
            depoimento = form.save(commit=False)
            depoimento.save()
            return redirect('listar_depoimentos')
    else:
        form = DepoimentoForm()
    return render(request, 'criar_depoimento.html', {'form': form})

def editar_depoimento(request, pk):
    depoimento = get_object_or_404(Depoimento, pk=pk)
    if request.method == 'POST':
        form = DepoimentoForm(request.POST, instance=depoimento)
        if form.is_valid():
            depoimento = form.save(commit=False)
            depoimento.save()
            return redirect('listar_depoimentos')
    else:
        form = DepoimentoForm(instance=depoimento)
    return render(request, 'editar_depoimento.html', {'form': form})

def excluir_depoimento(request, pk):
    depoimento = get_object_or_404(Depoimento, pk=pk)
    depoimento.delete()
    return redirect('listar_depoimentos')

def listar_depoimentos(request):
    depoimentos = Depoimento.objects.order_by('-data')
    return render(request, 'listar_depoimentos.html', {'depoimentos': depoimentos})

# Views de Endereço
def criar_endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save()
            return redirect('detalhes_endereco', pk=endereco.pk)
    else:
        form = EnderecoForm()
    return render(request, 'criar_endereco.html', {'form': form})

def editar_endereco(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            endereco = form.save()
            return redirect('detalhes_endereco', pk=endereco.pk)
    else:
        form = EnderecoForm(instance=endereco)
    return render(request, 'editar_endereco.html', {'form': form})

def excluir_endereco(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)
    endereco.delete()
    return redirect('lista_enderecos')
