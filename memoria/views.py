
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Partida
from datetime import datetime, timedelta
import random

# View de Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('jogo')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# View de Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# View do Jogo
@login_required
def jogo(request):
    if request.method == 'POST':
        tentativas = int(request.POST.get('tentativas'))
        tempo_inicio = datetime.strptime(request.POST.get('tempo_inicio'), "%Y-%m-%d %H:%M:%S")
        tempo_fim = datetime.now()
        tempo_total = tempo_fim - tempo_inicio

        # Salvar a partida no banco de dados
        Partida.objects.create(
            jogador=request.user,
            tentativas=tentativas,
            tempo=tempo_total,
            data_hora=tempo_fim
        )
        return redirect('ranking')

    cartas = list(range(1, 9)) * 2
    random.shuffle(cartas)

    return render(request, 'jogo.html', {
        'cartas': cartas,
        'tempo_inicio': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# View do Ranking
def ranking_view(request):
    partidas = Partida.objects.all().order_by('tentativas', '-data_hora')
    return render(request, 'ranking.html', {'partidas': partidas})
