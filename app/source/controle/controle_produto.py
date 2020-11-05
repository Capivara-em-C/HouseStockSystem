from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.entidade.produto_consumivel import ProdutoConsumivel
from app.source.entidade.estoque import Estoque
from app.source.limite.limite_produto import LimiteProduto
from app.source.helpers.setter import validacao_tipo


class ControleProduto(ControleAbstrato):
    @staticmethod
    def classe_limite() -> type:
        return LimiteProduto

    @staticmethod
    def classe_entidade() -> type:
        return ProdutoAbstrato

    def listar(self):
        rotas = self.rotas("listar")
        self.limite.listar(self.exportar_entidades())
        opcao = self.limite.selecionar_opcao("listar")[0]
        retorno = self.selecione_rota(rotas, opcao, self.listar)

        if retorno is not None:
            self.listar()

    def criar(self):
        rotas = self.rotas("criar")
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao("criar")

        self.adicionar_entidade(self.lista_para_produto(escolhas))

        self.selecione_rota(rotas, "v", self.listar)

    def voltar_listagem(self) -> None:
        return None

    @staticmethod
    def lista_para_produto(lista: list) -> ProdutoAbstrato:
        validacao_tipo(lista, list)
        if int(lista[6]) > 0:
            estoque = Estoque(
                "1",
                int(lista[6]),
                int(lista[7]),
            )

            return ProdutoConsumivel(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                None,
                float(lista[4]),
                int(lista[5]),
                estoque,
            )
