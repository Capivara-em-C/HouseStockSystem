from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo


class Categoria(EntidadeAbstrata):
    def __init__(self, identificador: int, nome: str):
        super().__init__(identificador)
        self.nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        validacao_tipo(nome, str)
        self.__nome = nome

    def objeto_limite(self) -> dict:
        return {
            "Nº Referencia": self.identificador,
            "Nome": self.nome,
        }
