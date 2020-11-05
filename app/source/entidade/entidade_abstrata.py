from abc import ABC, abstractmethod
from app.source.helpers.setter import validacao_tipo


class EntidadeAbstrata(ABC):
    def __init__(self, identificador: str):
        self.identificador = identificador

    @abstractmethod
    def objeto_limite(self) -> dict:
        pass

    @property
    def identificador(self) -> str:
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador: str):
        validacao_tipo(identificador, str)
        self.__identificador = identificador
