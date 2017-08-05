# -*- coding: UTF-8 -*-
#calculador_de_impostos.py
from impostos import ICMS, ISS

class Calculador_de_impostos(object):
	"""docstring for calculador_de_impostos"""

	
	def realiza_calculo(self, orcamento, calcula_imposto):
		imposto_calculado = calcula_imposto.calcula();
		print imposto_calculado

if __name__ == '__main__':
	
	from orcamento import Orcamento

	orcamento = Orcamento(500)
	calculador_de_impostos = Calculador_de_impostos()
	calculador_de_impostos.realiza_calculo(orcamento, ICMS())
	calculador_de_impostos.realiza_calculo(orcamento, ISS())
	