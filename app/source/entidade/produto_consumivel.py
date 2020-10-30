from app.source.entidade.estoque import Estoque
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.helpers.setter import validacao_tipo


class ProdutoConsumivel(ProdutoAbstrato):
    def __init__(
            self,
            identificador: int,
            nome: str = "",
            descricao: str = "",
            data_fabricacao: str = "",
            categorias: dict = None,
            ultimo_valor: float = 0,
            prioridade: int = 0,
            estoque: Estoque = None
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

        self.estoque = estoque

    @property
    def estoque(self) -> Estoque:
        return self.__estoque

    @estoque.setter
    def estoque(self, estoque: Estoque):
        validacao_tipo(estoque, Estoque)
        self.__estoque = estoque
