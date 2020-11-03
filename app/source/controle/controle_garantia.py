from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.limite.limite_inicio import LimiteInicio
from app.source.exception.rotaInexistenteException import RotaInexistenteException


class ControleGarantia(ControleAbstrato):

    @staticmethod
    def classe_limite():
        return LimiteInicio

    def rotas(self, nome_funcao):

        rota = {
            "home": {
                "a": self.nova_garantia,
                "r": self.listar_garantia,
                "d": self.deletar_garantia,
                "e": self.editar_garantia,
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

    def nova_compra(self):
        pass

    def consumir_estoque(self):
        pass

    def produto(self):
        pass
