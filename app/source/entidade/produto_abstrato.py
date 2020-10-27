from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_setter


class ProdutoAbstrato(EntidadeAbstrata):
    def __init__(
            self,
            identificador: int,
            nome: str = "",
            descricao: str = "",
            data_fabricacao: str = "",
            categorias: list = None,
            ultimo_valor: float = 0,
            prioridade: int = 0,
    ):
        super().__init__(identificador)

        if categorias is None:
            categorias = []

        self.nome = nome
        self.descricao = descricao
        self.data_fabricacao = data_fabricacao
        self.categorias = categorias
        self.ultimo_valor = ultimo_valor
        self.prioridade = prioridade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        validacao_setter(nome, str)
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        validacao_setter(descricao, str)
        self.__descricao = descricao

    @property
    def data_fabricacao(self) -> str:
        return self.__data_fabricacao

    @data_fabricacao.setter
    def data_fabricacao(self, data_fabricacao: str):
        validacao_setter(data_fabricacao, str)
        self.__data_fabricacao = data_fabricacao

    @property
    def categorias(self) -> list:
        return self.__categorias

    @categorias.setter
    def categorias(self, categorias: list):
        validacao_setter(categorias, list)
        self.__categorias = categorias

    @property
    def ultimo_valor(self) -> float:
        return self.__ultimo_valor

    @ultimo_valor.setter
    def ultimo_valor(self, ultimo_valor: float):
        validacao_setter(ultimo_valor, float)
        self.__ultimo_valor = ultimo_valor

    @property
    def prioridade(self) -> int:
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade: int):
        validacao_setter(prioridade, int)
        self.__prioridade = prioridade
