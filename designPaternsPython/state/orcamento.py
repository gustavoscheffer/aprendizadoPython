# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class Estados_de_um_Orcamento(object):
        
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()


class Em_Aprovacao(Estados_de_um_Orcamento):

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    
    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    
    def finaliza(self, orcamento):
        raise Exception('Não pode mudar de Em_Aprovacao para Finalizado!')

class Aprovado(Estados_de_um_Orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

class Reprovado(Estados_de_um_Orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception ('Orcamentos reprovados não recebem descontos')

class Finalizado(Estados_de_um_Orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception ('Orcamentos finalizados não recebem descontos')

class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_Aprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)
    
    def finaliza(self):
        self.estado_atual.finaliza(self)
    
    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor
        return total - self.__desconto_extra

    def obter_itens(self):

        return tuple(self.__itens)
    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome



if __name__ == '__main__':
    
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item-1',100))
    orcamento.adiciona_item(Item('Item-2',200))
    orcamento.adiciona_item(Item('Item-3',100))
 
    print 'Valor sem desconto => %s' % (orcamento.valor)

    orcamento.aplica_desconto_extra()
    print 'Valor com desconto extra(Em_Aprovacao) => %s' % (orcamento.valor)

    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print 'Valor com desconto extra(Aprovado) => %s' % (orcamento.valor)
