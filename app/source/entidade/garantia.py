from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo
from datetime import date

class Garantia(EntidadeAbstrata):

    def __init__(
            self,
            identificador: int,
            data_criacao: date,
            data_validade: date,
            documento: str,
            codigo: str,
            numero_serie:str,
    ):
        super.__init__(identificador)
        self.data_criacao = data_criacao
        self.data_validade = data_validade
        self.documento = documento
        self.codigo = codigo
        self.numero_serie = numero_serie

    def retorna_garantia(self):
        garantia = "Data criação: " + self.data_criacao + "\n Data validade: " + self.data_validade + "\n Documento: " + self.documento + "\n Código: " + self.codigo + "\n Número de Série: " + self.numero_serie
        return garantia

    @property
    def data_criacao(self):
        return self.data_criacao

    @data_criacao.setter
    def data_criacao(self,data):
        validacao_tipo(data, date)
        self.data_criacao = data

    @property
    def data_validade(self):
        return self.data_validade

    @data_validade.setter
    def data_validade(self, data):
        validacao_tipo(data, date)
        self.data_validade = data

    @property
    def documento(self):
        return self.documento

    @documento.setter
    def documento(self, documento):
        validacao_tipo(documento, str)
        self.documento = documento

    @property
    def codigo(self):
        return self.codigo

    @data_criacao.setter
    def codigo(self, codigo):
        validacao_tipo(codigo, str)
        self.codigo = codigo

    @property
    def numero_serie(self):
        return self.numero_serie

    @numero_serie.setter
    def numero_serie(self, numero):
        validacao_tipo(numero, str)
        self.numero_serie = numero