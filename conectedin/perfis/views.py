from django.shortcuts import render

from perfis.models import Perfil


def index(request):
    return render(request, 'index.html')


def exibir(request, perfil_id):
	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil('Izabela Guerreiro', 'izaguerreiro@gmail.com',  '222222', 'Izepa')

	if perfil_id == '2':
		perfil = Perfil('Paulo Roberto', 'paulo.pinda@gmail.com',  '2222', 'Izepa')

	return render(request, 'perfil.html', {'perfil': perfil})