from app.source.persistencia.DAO_abstrato import DAOabstrato
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.helpers.setter import validacao_tipo


class DAOproduto(DAOabstrato):

    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto: ProdutoAbstrato):
        validacao_tipo(produto, ProdutoAbstrato)
        super().add(ProdutoAbstrato.identificador, produto)

    def get(self, identificador):
        return super().get(identificador)

    def remove(self, identificador):
        return super().remove(identificador)
