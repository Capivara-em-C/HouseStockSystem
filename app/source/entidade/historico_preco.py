from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo
from datetime import date

class HistoricoPreco(EntidadeAbstrata):

    def __init__(
            self,
            identificador: int,
            valor: float,
            data_valor: str
    ):
        super.__init__(identificador)
        self.__valor = valor
        self.__data_valor = data_valor

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor):
        validacao_tipo(valor, float)
        self.__valor = valor

    @property
    def data_valor(self) -> str:
        return self.__data_valor


    @data_valor.setter
    def valor(self, valor):
        validacao_tipo(valor, float)
        self.__valor = valor
