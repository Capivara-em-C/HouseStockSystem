from app.source.persistencia.DAO_abstrato import DAOAbstrato
from app.source.entidade.categoria import Categoria
from app.source.helpers.setter import validacao_tipo


class DAOCategoria(DAOAbstrato):

    def __init__(self):
        super().__init__('categorias.pkl')
