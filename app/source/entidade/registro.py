from app.source.helpers.setter import validacao_tipo


class Registro():

    def __init__(
            self,
            acao: str,
            hora: str
    ):
        self.acao = acao
        self.hora = hora

    @property
    def acao(self) -> str:
        return self.__acao

    @acao.setter
    def acao(self, acao: str):
        validacao_tipo(acao, str)
        self.__acao = acao

    @property
    def hora(self) -> str:
        return self.__hora

    @hora.setter
    def hora(self, hora: str):
        validacao_tipo(hora, str)
        self.__hora = hora