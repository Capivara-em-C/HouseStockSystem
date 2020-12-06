from app.source.persistencia.DAO_abstrato import DAOabstrato
from app.source.entidade.categoria import Categoria
from app.source.helpers.setter import validacao_tipo


class DAOcategoria(DAOabstrato):

    def __init__(self):
        super().__init__('categorias.pkl')

    def add(self, categoria: Categoria):
        validacao_tipo(categoria, Categoria)
        super().add(categoria.identificador, categoria)

    def get(self, identificador):
        return super().get(identificador)

    def remove(self, identificador):
        return super().remove(identificador)
