from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo


class Estoque(EntidadeAbstrata):
    def __init__(self, identificador: int, quantidade: int, estoque_minimo: int):
        super().__init__(identificador)
        self.quantidade = quantidade
        self.estoque_minimo = estoque_minimo

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        validacao_tipo(quantidade, int)
        self.__quantidade = quantidade

    @property
    def estoque_minimo(self):
        return self.__estoque_minimo

    @estoque_minimo.setter
    def estoque_minimo(self, estoque_minimo: int):
        validacao_tipo(estoque_minimo, int)
        self.__estoque_minimo = estoque_minimo
