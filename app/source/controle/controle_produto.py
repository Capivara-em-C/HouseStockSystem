from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.limite.limite_produto import LimiteProduto


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
        opcao = self.limite.selecionar_opcao()[0]
        self.selecione_rota(rotas, opcao, self.listar)

    def voltar_listagem(self) -> None:
        return None
