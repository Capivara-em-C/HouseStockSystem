from abc import ABC
from app.source.helpers.setter import validacao_tipo


class EntidadeAbstrata(ABC):
    def __init__(self, identificador: str):
        self.identificador = identificador

    def objeto_limite(self) -> dict:
        pass

    def objeto_limite_detalhado(self) -> dict:
        pass

    @property
    def identificador(self) -> str:
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador: str):
        validacao_tipo(identificador, str)
        self.__identificador = identificador
