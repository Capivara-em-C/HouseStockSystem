from app.source.helpers.setter import validacao_tipo
from datetime import datetime


class Registro():
    def __init__(
            self,
            titulo: str,
            requisicao: str,
    ):
        self.hora = str(datetime.now())
        self.titulo = titulo
        self.requisicao = requisicao

    @property
    def hora(self) -> str:
        return self.__hora

    @hora.setter
    def hora(self, hora: str):
        validacao_tipo(hora, str)
        self.__hora = hora

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        validacao_tipo(titulo, str)
        self.__titulo = titulo

    @property
    def requisicao(self) -> str:
        return self.__requisicao

    @requisicao.setter
    def requisicao(self, requisicao: str):
        validacao_tipo(requisicao, str)
        self.__requisicao = requisicao
