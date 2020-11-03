from abc import ABC
from app.source.helpers.setter import validacao_tipo


class EntidadeAbstrata(ABC):
    def __init__(self, identificador: int):
        self.identificador = identificador

    @property
    def identificador(self) -> int:
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador: int):
        validacao_tipo(identificador, int)
        self.__identificador = identificador