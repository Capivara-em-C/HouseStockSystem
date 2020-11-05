from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.limite.limite_categoria import LimiteCategoria
from app.source.exception.rotaInexistenteException import RotaInexistenteException


class ControleCategoria(ControleAbstrato):

    @staticmethod
    def classe_limite() -> type:
        return LimiteCategoria

    def listar(self):
        rotas = self.rotas("listar")
        self.limite.listar(self.exportar_entidades())
        opcao = self.limite.selecionar_opcao("listar")["menu"]
        retorno = self.selecione_rota(rotas, opcao, self.listar)

        if retorno is not None:
            self.listar()

    def criar(self):
        rotas = self.rotas("criar")
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao("criar")

        self.adicionar_entidade(self.PRODUTO_ENTIDADE, self.lista_para_produto(escolhas))

        self.selecione_rota(rotas, "v", self.listar)

    def atualizar(self):
        rotas = self.rotas("atualizar")
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao("atualizar")

        self.atualizar_entidade(self.PRODUTO_ENTIDADE, self.lista_para_produto(escolhas))

        self.selecione_rota(rotas, "v", self.listar)

    def deletar(self):
        rotas = self.rotas("deletar")
        self.limite.criar()
        escolha = self.limite.selecionar_opcao("deletar")["codigo_referencia"]

        self.remover_entidade(self.PRODUTO_ENTIDADE, self.entidades[self.PRODUTO_ENTIDADE].get(escolha))

        self.selecione_rota(rotas, "v", self.listar)

    def voltar_listagem(self) -> None:
        return None
