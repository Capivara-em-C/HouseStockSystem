from app.source.persistencia.DAO_abstrato import DAOAbstrato


class DAOCategoria(DAOAbstrato):
    def __init__(self):
        super().__init__('categorias')
