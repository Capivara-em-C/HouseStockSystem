from app.source.entidade.produto_consumivel import ProdutoConsumivel
from app.source.entidade.estoque import Estoque
from app.source.entidade.lote import Lote
from app.source.helpers.setter import validacao_tipo


class ProdutoPerecivel(ProdutoConsumivel):
    def __init__(
            self,
            identificador: int,
            nome: str = "",
            descricao: str = "",
            data_fabricacao: str = "",
            categorias: dict = None,
            ultimo_valor: float = 0,
            prioridade: int = 0,
            estoque: Estoque = None,
            lotes: dict = None
    ):
        super().__init__(
            identificador,
            nome,
            descricao,
            data_fabricacao,
            categorias,
            ultimo_valor,
            prioridade,
            estoque
        )

        self.lotes = lotes

    @property
    def lotes(self):
        return self.__lotes

    @lotes.setter
    def lotes(self, lotes: dict):
        validacao_tipo(lotes, dict)
        self.__lotes = lotes
        self.atualizar_estoque()

    def add_lote(self, lote: Lote):
        validacao_tipo(lote, Lote)
        self.__lotes[lote.identificador] = lote
        self.atualizar_estoque()

    def remover_lote(self, lote: Lote):
        validacao_tipo(lote, Lote)
        del(self.__lotes[lote.identificador])
        self.atualizar_estoque()

    def atualizar_estoque(self):
        self.estoque.quantidade = self.quantidade_total()

    def quantidade_total(self):
        quantidade_total = 0

        for lote in self.lotes:
            quantidade_total += lote.quantidade

        return quantidade_total
