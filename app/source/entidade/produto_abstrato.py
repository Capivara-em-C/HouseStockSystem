from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.helpers.setter import validacao_tipo
from abc import abstractmethod


class ProdutoAbstrato(EntidadeAbstrata):
    @abstractmethod
    def __init__(
            self,
            identificador: str,
            nome: str = "",
            descricao: str = "",
            data_fabricacao: str = "",
            categorias: dict = None,
            ultimo_valor: float = 0,
            prioridade: int = 0,
    ):
        super().__init__(identificador)

        if categorias is None:
            categorias = {}

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
        self.__categorias = categorias

    # @TODO fazer o link entre entidade Categorias
    def adicionar_categoria(self, categoria: dict):
        validacao_tipo(categoria, dict)
        self.__categorias[categoria["identificador"]] = categoria

    def remover_categoria(self, categoria: dict):
        validacao_tipo(categoria, dict)
        del self.__categorias[categoria["identificador"]]

    def existe_categoria(self, categoria: dict) -> bool:
        validacao_tipo(categoria, dict)
        return categoria["identificador"] in self.__categorias.keys()

    @property
    def ultimo_valor(self) -> float:
        return self.__ultimo_valor

    @ultimo_valor.setter
    def ultimo_valor(self, ultimo_valor: float):
        validacao_tipo(ultimo_valor, float)
        self.__ultimo_valor = ultimo_valor

    @property
    def prioridade(self) -> int:
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade: int):
        validacao_tipo(prioridade, int)
        self.__prioridade = prioridade

    def objeto_limite(self) -> dict:
        return {
            "Nº Referencia": self.identificador,
            "Nome": self.nome,
            "Último valor": self.ultimo_valor,
        }

    def objeto_limite_detalhado(self) -> dict:
        return {
            "Nº Referencia": self.identificador,
            "Nome": self.nome,
            "Descrição": self.descricao,
            "Data de Fabricação": self.data_fabricacao,
            "Categorias": self.categorias,
            "Último valor pago": self.ultimo_valor,
        }
