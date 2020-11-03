from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo
from datetime import date

class HistoricoPreco(EntidadeAbstrata):

    def __init__(self,identificador: int, valor: float, data_valor: date):
        super.__init__(identificador)
        self.valor = valor
        self.data_valor = date

    @property
    def valor(self):
        return self.valor

    @valor.setter
    def valor(self, valor):
        validacao_tipo(valor, float)
        self.valor = valor

    @property
    def data_valor(self):
        return self.data_valor

    @data_valor.setter
    def valor(self, valor):
        validacao_tipo(valor, float)
        self.valor = valor