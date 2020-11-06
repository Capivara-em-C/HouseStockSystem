from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo


class Lote(EntidadeAbstrata):
    def __init__(
            self,
            data_validade: str,
            quantidade: int,
    ):
        super().__init__(data_validade)
        self.quantidade = quantidade

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        validacao_tipo(quantidade, int)
        self.__quantidade = quantidade

    @property
    def data_validade(self) -> str:
        return self.identificador

    @data_validade.setter
    def data_validade(self, data_validade: str):
        validacao_tipo(data_validade, str)
        self.identificador = data_validade

    def objeto_limite(self) -> dict:
        return {
            "Data de validade": self.data_validade,
            "Quantidade": self.quantidade,
        }
