#-*- coding: UTF-8 -*-
#calculador_de_descontos.py

from desconto import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):
	"""docstring for calculador_de_descontos"""
	
	def calcula(self, orcamento):
		desconto = Desconto_por_mais_de_quinhentos_reais(
			Desconto_por_cinco_itens(
				Sem_desconto()
				)
			)
		return desconto.calcula(orcamento)



if __name__ == '__main__':
	
	from orcamento import Orcamento, Item

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('Item-1',100))
	orcamento.adiciona_item(Item('Item-2',50))
	orcamento.adiciona_item(Item('Item-3',800))

	calculador_de_descontos = Calculador_de_descontos()
	valor_descontado = calculador_de_descontos.calcula(orcamento)	

	print 'O valor do desconto será => %s' % (valor_descontado) 


