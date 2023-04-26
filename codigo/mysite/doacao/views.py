from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doacao, Peruca
from .forms import DoacaoForm, PerucaForm

# views de doação
@login_required
def solicitarDoacao(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doacao')
    else:
        form = DoacaoForm()
    return render(request, 'solicitar_doacao.html', {'form': form})

@login_required
def cancelarSolicitacao(request, id):
    doacao = Doacao.objects.get(id=id)
    doacao.delete()
    return redirect('listar_doacao')

def analisarSolicitacao(request, id, status):
    doacao = Doacao.objects.get(id=id)
    doacao.status = status
    doacao.save()
    return redirect('listar_doacao')

def listarDoacao(request):
    doacoes = Doacao.objects.all().order_by('data')
    return render(request, 'listar_doacoes.html', {'doacoes': doacoes})

# views de peruca
def criar_peruca(request):
    if request.method == 'POST':
        form = PerucaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_perucas')
    else:
        form = PerucaForm()
    return render(request, 'criar_peruca.html', {'form': form})

def editar_peruca(request, id):
    peruca = get_object_or_404(Peruca, pk=id)
    if request.method == 'POST':
        form = PerucaForm(request.POST, instance=peruca)
        if form.is_valid():
            form.save()
            return redirect('listar_perucas')
    else:
        form = PerucaForm(instance=peruca)
    return render(request, 'editar_peruca.html', {'form': form})

def excluir_peruca(request, id):
    peruca = get_object_or_404(Peruca, pk=id)
    peruca.delete()
    return redirect('listar_perucas')

def listar_perucas(request):
    perucas = Peruca.objects.all().order_by('tamanho')
    return render(request, 'listar_perucas.html', {'perucas': perucas})
