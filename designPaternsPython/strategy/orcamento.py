# -*- coding: UTF-8 -*-
# class orcamento


class Orcamento(object):
	def __init__(self, valor):
		self._valor = valor

	@property
	def valor(self):
	    return self._valor
	@valor.setter
	def valor(self, value):
	    self._valor = value
	
		