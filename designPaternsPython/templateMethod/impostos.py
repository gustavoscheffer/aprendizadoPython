from abc import ABCMeta, abstractmethod


class Template_impostos_condicionais(object):
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
			
			return self.concede_desc_max(orcamento)
		
		return self.concede_desc_min(orcamento)	

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

class ICPP(Template_impostos_condicionais):
	"""docstring for ICPP"""

	def deve_receber_desconto_max(self,orcamento):
		return orcamento.valor > 500

	def concede_desc_max(self,orcamento):
		return orcamento.valor * 0.07
	
	def concede_desc_min(self,orcamento):
		return orcamento.valor * 0.05

class ISS(object):

	def calcula(self, orcamento):

		return orcamento.valor * 0.1

class ICMS(object):

	def calcula(self, orcamento):
		return orcamento.valor * 0.06	
	

								