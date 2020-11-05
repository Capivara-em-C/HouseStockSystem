from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.limite.limite_inicio import LimiteInicio
from app.source.exception.rotaInexistenteException import RotaInexistenteException
from app.source.controle.controle_produto import ControleProduto
from app.source.limite.limite_produto import LimiteProduto


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
        opcao = self.limite.selecionar_opcao("home")["menu"]
        self.selecione_rota(rotas, opcao, self.home)
        self.home()

    def nova_compra(self):
        pass

    def consumir_estoque(self):
        pass

    def produto(self):
        controle_produto = ControleProduto(LimiteProduto())
        controle_produto.entidades = self.entidades
        controle_produto.listar()
        self.entidades = controle_produto.entidades
