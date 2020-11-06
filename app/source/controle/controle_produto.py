from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_lote import ControleLote
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.entidade.produto_consumivel import ProdutoConsumivel
from app.source.entidade.produto_perecivel import ProdutoPerecivel
from app.source.limite.limite_produto import LimiteProduto
from app.source.limite.limite_lote import LimiteLote
from app.source.helpers.setter import validacao_tipo


class ControleProduto(ControleAbstrato):
    @staticmethod
    def classe_limite() -> type:
        return LimiteProduto

    @staticmethod
    def classe_entidade() -> type:
        return ProdutoAbstrato

    def listar(self):
        nome_funcao = "listar"

        rotas = self.rotas(nome_funcao)
        self.limite.listar(self.exportar_entidades())

        opcao = self.limite.selecionar_opcao(nome_funcao)["menu"]
        retorno = self.selecione_rota(rotas, opcao, self.listar)

        if retorno is not None:
            self.listar()

    def criar(self):
        nome_funcao = "criar"

        rotas = self.rotas(nome_funcao)
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao(nome_funcao)
        produto = self.lista_para_produto(escolhas)

        produto.lotes = ControleLote(LimiteLote()).listar()

        self.adicionar_entidade(self.PRODUTO_ENTIDADE, produto)

        self.selecione_rota(rotas, "v", self.listar)

    def atualizar(self):
        nome_funcao = "atualizar"
        rotas = self.rotas(nome_funcao)
        self.limite.atualizar()
        escolhas = self.limite.selecionar_opcao(nome_funcao)
        produto = self.lista_para_produto(escolhas)

        self.atualizar_entidade(self.PRODUTO_ENTIDADE, produto)

        self.selecione_rota(rotas, "v", self.listar)

    def mostrar(self):
        nome_funcao = "mostrar"
        rotas = self.rotas(nome_funcao)
        escolha = self.limite.selecionar_opcao(nome_funcao)["codigo_referencia"]

        produto = self.entidades[self.PRODUTO_ENTIDADE].get(escolha).objeto_limite_detalhado()
        if produto.get("lotes") is not None:
            produto["lotes"] = self.lotes_para_limite(produto["lotes"])

        self.limite.mostrar(produto)

        self.selecione_rota(rotas, "v", self.listar)

    def deletar(self):
        nome_funcao = "deletar"

        rotas = self.rotas(nome_funcao)

        escolha = self.limite.selecionar_opcao(nome_funcao)["codigo_referencia"]
        self.remover_entidade(self.PRODUTO_ENTIDADE, self.entidades[self.PRODUTO_ENTIDADE].get(escolha))

        self.selecione_rota(rotas, "v", self.listar)

    def voltar_listagem(self) -> None:
        return None

    @staticmethod
    def lista_para_produto(lista: dict) -> ProdutoAbstrato:
        validacao_tipo(lista, dict)

        if int(lista["estoque"]) > 0:
            return ProdutoPerecivel(
                lista["codigo_referencia"],
                lista["nome"],
                lista["descricao"],
                lista["data_fabricacao"],
                None,
                float(lista["valor"]),
                int(lista["prioridade"]),
                int(lista["estoque"]),
                int(lista["estoque_minimo"]),
            )

    @staticmethod
    def lotes_para_limite(lotes: dict):
        validacao_tipo(lotes, dict)

        resp = {}
        for chave in lotes:
            lote = lotes[chave]
            resp[chave] = lote.objeto_limite()

        return resp
