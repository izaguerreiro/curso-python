# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View


class RegistrarUsuarioView(View):
	
	template_name = 'registrar.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
        #preencher o from
        form = RegistrarUsuarioForm(request.POST)
        
        #verificando se eh validor
        if form.is_valid():
            dados_form = form.data
            #criar o usuario
            usuario = User.objects.create_user(dados_form['email'], dados_form['email'], dados_form['senha'])            
            #criar o perfil
            perfil = Perfil(nome=dados_form['nome'], 
                            email=dados_form['email'], 
                            telefone=dados_form['telefone'],
                            nome_empresa=dados_form['nome_empresa'],
                            usuario=usuario)
            #gravar no banco
            perfil.save()
            #redirecioando para index
            return redirect('index')

        return render(request, self.template_name, {'form': form})