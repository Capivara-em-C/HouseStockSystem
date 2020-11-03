from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.limite.limite_inicio import LimiteInicio
from app.source.exception.rotaInexistenteException import RotaInexistenteException


class ControleCategoria(ControleAbstrato):

    @staticmethod
    def classe_limite():
        return LimiteInicio

    def rotas(self, nome_funcao):
        rota = {
            "home": {
                "n": self.nova_categoria,
                "l": self.listar_categoria,
                "d": self.deletar_categoria,
                "e": self.editar_categoria,
                "s": exit,
            },
        }

        try:
            return rota[nome_funcao]
        except KeyError:
            raise RotaInexistenteException("Rota passada não existente.")

    def home(self):
        rotas = self.rotas("home")
        self.limite.home()
        opcao = self.limite.selecionar_opcao()[0]
        self.selecione_opcao(rotas, opcao, self.home)

    def nova_categoria(self):
        pass

    def listar_categoria(self):
        pass

    def editar_categoria(self):
        pass

    def deletar_categoria(self):
        pass


