from abc import abstractmethod

from app.source.entidade.categoria import Categoria
from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo


class ProdutoAbstrato(EntidadeAbstrata):
    @abstractmethod
    def __init__(
            self,
            identificador: str,
            nome: str = "",
            descricao: str = "",
            data_fabricacao: str = "",
            categorias: dict = None,
            valor: float = 0,
            prioridade: int = 0,
    ):
        super().__init__(identificador)

        if categorias is None:
            categorias = {}

        self.nome = nome
        self.descricao = descricao
        self.data_fabricacao = data_fabricacao
        self.categorias = categorias
        self.valor = valor
        self.prioridade = prioridade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        validacao_tipo(nome, str)
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        validacao_tipo(descricao, str)
        self.__descricao = descricao

    @property
    def data_fabricacao(self) -> str:
        return self.__data_fabricacao

    @data_fabricacao.setter
    def data_fabricacao(self, data_fabricacao: str):
        validacao_tipo(data_fabricacao, str)
        self.__data_fabricacao = data_fabricacao

    @property
    def categorias(self) -> dict:
        return self.__categorias

    @categorias.setter
    def categorias(self, categorias: dict):
        validacao_tipo(categorias, dict)

        for categoria in categorias.values():
            validacao_tipo(categoria, Categoria)

        self.__categorias = categorias

    def adicionar_categoria(self, categoria: Categoria):
        validacao_tipo(categoria, Categoria)
        self.__categorias[categoria.identificador] = categoria

    def remover_categoria(self, categoria: Categoria):
        validacao_tipo(categoria, Categoria)
        del self.__categorias[categoria.identificador]

    def existe_categoria(self, categoria: Categoria) -> bool:
        validacao_tipo(categoria, Categoria)
        return self.categorias[categoria.identificador] in self.__categorias.keys()

    @property
    def valor(self) -> float:
        return self.__ultimo_valor

    @valor.setter
    def valor(self, ultimo_valor: float):
        validacao_tipo(ultimo_valor, float)
        self.__ultimo_valor = ultimo_valor

    @property
    def prioridade(self) -> int:
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade: int):
        validacao_tipo(prioridade, int)
        self.__prioridade = prioridade

    def objeto_limite(self) -> list:
        return [
            self.identificador,
            self.nome,
        ]

    def objeto_limite_detalhado(self) -> dict:
        return {
            "codigo": self.identificador,
            "nome": self.nome,
            "descricao": self.descricao,
            "data_fabricação": self.data_fabricacao,
            "valor": self.valor,
            "categorias": self.categorias_limite(),
        }

    def categorias_limite(self) -> dict:
        resp = {}

        for chave in self.categorias:
            categoria = self.categorias[chave]
            resp[chave] = categoria.objeto_limite()

        return resp
