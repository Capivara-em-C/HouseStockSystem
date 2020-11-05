from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo
from strtime import str

class Garantia(EntidadeAbstrata):

    def __init__(
            self,
            identificador: int,
            data_criacao: str,
            data_validade: str,
            documento: str,
            codigo: str,
            numero_serie: str,
    ):
        super.__init__(identificador)
        self.data_criacao = data_criacao
        self.data_validade = data_validade
        self.documento = documento
        self.codigo = codigo
        self.numero_serie = numero_serie

    def retorna_garantia(self) -> str:
        garantia = "Data criação: " + self.data_criacao() +\
                   "\n Data validade: " + self.data_validade() +\
                   "\n Documento: " + self.documento() +\
                   "\n Código: " + self.codigo() +\
                   "\n Número de Série: " + self.numero_serie()
        return garantia

    @property
    def data_criacao(self) -> str:
        return self.__data_criacao

    @data_criacao.setter
    def data_criacao(self, data: str):
        validacao_tipo(data, str)
        self.__data_criacao = data

    @property
    def data_validade(self) -> str:
        return self.__data_validade

    @data_validade.setter
    def data_validade(self, data: str):
        validacao_tipo(data, str)
        self.__data_validade = data

    @property
    def documento(self) -> str:
        return self.__documento

    @documento.setter
    def documento(self, documento: str):
        validacao_tipo(documento, str)
        self.__documento = documento

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):
        validacao_tipo(codigo, str)
        self.__codigo = codigo

    @property
    def numero_serie(self) -> str:
        return self.__numero_serie

    @numero_serie.setter
    def numero_serie(self, numero: str):
        validacao_tipo(numero, str)
        self.__numero_serie = numero
