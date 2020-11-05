from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.helpers.setter import validacao_tipo


class ProdutoConsumivel(ProdutoAbstrato):
    def __init__(
            self,
            identificador: str,
            nome: str = "",
            descricao: str = "",
            data_fabricacao: str = "",
            categorias: dict = None,
            ultimo_valor: float = 0,
            prioridade: int = 0,
            estoque_quantidade: int = 0,
            estoque_minimo: int = 0
    ):
        super().__init__(
            identificador,
            nome,
            descricao,
            data_fabricacao,
            categorias,
            ultimo_valor,
            prioridade
        )

        self.estoque_quantidade = estoque_quantidade
        self.estoque_minimo = estoque_minimo

    @property
    def estoque_quantidade(self) -> int:
        return self.__estoque_quantidade

    @estoque_quantidade.setter
    def estoque_quantidade(self, estoque_quantidade: int):
        validacao_tipo(estoque_quantidade, int)
        self.__estoque_quantidade = estoque_quantidade

    @property
    def estoque_minimo(self) -> int:
        return self.__estoque_minimo

    @estoque_minimo.setter
    def estoque_minimo(self, estoque_minimo: int):
        validacao_tipo(estoque_minimo, int)
        self.__estoque_minimo = estoque_minimo
