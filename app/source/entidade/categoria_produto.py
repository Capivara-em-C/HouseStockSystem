from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo


class Categoria(EntidadeAbstrata):

    def __init__(self,identificador: int, nome: str):
        super.__init__(identificador)
        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        validacao_tipo(nome, str)
        self.__nome = nome