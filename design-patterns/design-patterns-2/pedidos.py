# -*- coding: utf-8 -*-

from datetime import date
from abc import ABCMeta, abstractmethod

class Pedido(object):
	def __init__(self, cliente, valor):
		self.__cliente = cliente
		self.__valor = valor
		self.__status = "NOVO"
		self.__data_finalizado = None

	@property
	def cliente(self):
		return self.__cliente

	@property
	def valor(self):
		return self.__valor

	@property
	def status(self):
		return self.__status

	@property
	def data_finalizado(self):
		return self.__data_finalizado

	def paga(self):
		self.__status = "PAGO"

	def finaliza(self):
		self.__data_finalizado = date.today()
		self.__status = "ENTREGUE"


class Comando(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def executa(self):
		pass


class ConcluiPedido(Comando):
	def __init__(self, pedido):
		self.__pedido = pedido

	def executa(self):
		self.__pedido.finaliza()


class PagaPedido(Comando):
	def __init__(self, pedido):
		self.__pedido = pedido

	def executa(self):
		self.__pedido.paga()


class FilaTrabalho(object):
	def __init__(self):
		self.__comandos = []

	def adiciona(self, comando):
		self.__comandos.append(comando)

	def processa(self):
		for comando in self.__comandos:
			comando.executa()


if __name__ == "__main__":
	pedido1 = Pedido("Izabela", 200)
	pedido2 = Pedido("Paulo", 400)

	fila_de_trabalho = FilaTrabalho()
	fila_de_trabalho.adiciona(ConcluiPedido(pedido1))
	fila_de_trabalho.adiciona(PagaPedido(pedido1))
	fila_de_trabalho.adiciona(ConcluiPedido(pedido2))
	fila_de_trabalho.processa()