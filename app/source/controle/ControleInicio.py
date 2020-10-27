from app.source.controle.ControleAbstrato import ControleAbstrato
from app.source.limite.LimiteInicio import LimiteInicio
from app.source.Exception.RotaInexistenteException import RotaInexistenteException


class ControleInicio(ControleAbstrato):

    @staticmethod
    def classe_limite():
        return LimiteInicio

    def rotas(self, nome_funcao):
        rota = {
            "home": {
                "a": self.nova_compra,
                "r": self.consumir_estoque,
                "p": self.produto,
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
