from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.entidade.produto_consumivel import ProdutoConsumivel
from app.source.limite.limite_produto import LimiteProduto
from app.source.helpers.setter import validacao_tipo
from app.source.controle.controle_categoria import Categoria, ControleCategoria
from app.source.helpers.existe_categoria import existe_categoria
import string
import random


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

        self.adicionar_entidade(self.PRODUTO_ENTIDADE, self.lista_para_produto(escolhas))

        self.selecione_rota(rotas, "v", self.listar)

    def atualizar(self):
        nome_funcao = "atualizar"

        rotas = self.rotas(nome_funcao)
        self.limite.atualizar()
        escolhas = self.limite.selecionar_opcao(nome_funcao)

        self.atualizar_entidade(self.PRODUTO_ENTIDADE, self.lista_para_produto(escolhas))

        self.selecione_rota(rotas, "v", self.listar)

    def mostrar(self):
        nome_funcao = "mostrar"

        rotas = self.rotas(nome_funcao)

        escolha = self.limite.selecionar_opcao(nome_funcao)["codigo_referencia"]
        produto = self.entidades[self.PRODUTO_ENTIDADE].get(escolha)
        self.limite.mostrar(produto.objeto_limite_detalhado())

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

        if existe_categoria(lista['categoria'], ControleAbstrato.entidades):
            if int(lista["estoque"]) > 0:
                return ProdutoConsumivel(
                    lista["codigo_referencia"],
                    lista["nome"],
                    lista["descricao"],
                    lista["data_fabricacao"],
                    float(lista["valor"]),
                    int(lista["prioridade"]),
                    lista["categoria"],
                    int(lista["estoque"]),
                    int(lista["estoque_minimo"]),
                )
        else:
            letras = string.ascii_uppercase
            codigo = ''.join(random.choice(letras) for _ in range(4))
            ControleCategoria.entidades[codigo] = Categoria(random.randint(100, 1000), lista["categoria"])
            if int(lista["estoque"]) > 0:
                return ProdutoConsumivel(
                    lista["codigo_referencia"],
                    lista["nome"],
                    lista["descricao"],
                    lista["data_fabricacao"],
                    float(lista["valor"]),
                    int(lista["prioridade"]),
                    lista["categoria"],
                    int(lista["estoque"]),
                    int(lista["estoque_minimo"]),
                )
