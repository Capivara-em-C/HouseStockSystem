from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo


class Lote(EntidadeAbstrata):
    def __init__(
            self,
            identificador: int,
            quantidade: int,
            data_validade: str
    ):
        super().__init__(identificador)
        self.quantidade = quantidade,
        self.data_validade = data_validade

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        validacao_tipo(quantidade, int)
        self.__quantidade = quantidade

    @property
    def data_validade(self) -> str:
        return self.__data_validade

    @data_validade.setter
    def data_validade(self, data_validade: str):
        validacao_tipo(data_validade, str)
        self.__data_validade = data_validade
