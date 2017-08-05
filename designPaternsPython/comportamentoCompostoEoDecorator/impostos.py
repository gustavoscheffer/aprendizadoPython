from abc import ABCMeta, abstractmethod

class Imposto(object):
	
	__metaclass__ = ABCMeta

	def __init__(self, outro_imposto=None):
		self.__outro_imposto = outro_imposto
	
	def calcula_outro_imposto(self, orcamento):
		if self.__outro_imposto is not None:
			return self.__outro_imposto.calcula(orcamento)
		return 0	

	@abstractmethod
	def calcula(self):
		pass

class Template_impostos_condicionais(Imposto):
	"""Template_impostos_condicionais"""
	
	__metaclass__ = ABCMeta

	
	@abstractmethod	
	def deve_receber_desconto_max(self,orcamento):
		pass

	@abstractmethod
	def concede_desc_max(self,orcamento):
		pass
	
	@abstractmethod
	def concede_desc_min(self,orcamento):
		pass

	
	def calcula(self, orcamento):
		if self.deve_receber_desconto_max(orcamento):
			
			return self.concede_desc_max(orcamento) + self.calcula_outro_imposto(orcamento)
		
		return self.concede_desc_min(orcamento) + self.calcula_outro_imposto(orcamento)	

class ISS(Imposto):

	def calcula(self, orcamento):

		return orcamento.valor * 0.1 + self.calcula_outro_imposto(orcamento) 

class ICMS(Imposto):

	def calcula(self, orcamento):
		return orcamento.valor * 0.06 + self.calcula_outro_imposto(orcamento)

class ICPP(Template_impostos_condicionais):
	"""docstring for ICPP"""

	def deve_receber_desconto_max(self,orcamento):
		return orcamento.valor > 500

	def concede_desc_max(self,orcamento):
		return orcamento.valor * 0.07 
	
	def concede_desc_min(self,orcamento):
		return orcamento.valor * 0.05
	
class IKCV(Template_impostos_condicionais):
	"""docstring for IKCV"""	

	def deve_receber_desconto_max(self,orcamento):
		return orcamento.valor > 500 and __tem_item_maior_100_reias()

	def concede_desc_max(self,orcamento):
		return orcamento.valor * 0.10 
	
	def concede_desc_min(self,orcamento):
		return orcamento.valor * 0.06 
	
	def __tem_item_maior_100_reias(self,orcamento):
		""" Private Method - helper Method """
		for item in orcamento.obter_itens():
			if item > 100:
				return True
			return False											