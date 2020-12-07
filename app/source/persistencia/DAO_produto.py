from app.source.persistencia.DAO_abstrato import DAOAbstrato
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.helpers.setter import validacao_tipo


class DAOProduto(DAOAbstrato):

    def __init__(self):
        super().__init__('produtos')

    def add(self, identificador: str, produto: ProdutoAbstrato):
        validacao_tipo(produto, ProdutoAbstrato)
        super().add(produto.identificador, produto)
