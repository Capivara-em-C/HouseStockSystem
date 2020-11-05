from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo


class Estoque(EntidadeAbstrata):
    def __init__(self, identificador: str, quantidade: int, estoque_minimo: int):
        super().__init__(identificador)

    def objeto_limite(self) -> dict:
        return {

        }
