from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.limite.limite_lote import LimiteLote
from app.source.entidade.lote import Lote
from app.source.helpers.setter import validacao_tipo


class ControleLote(ControleAbstrato):
    @staticmethod
    def classe_limite() -> type:
        return LimiteLote

    @staticmethod
    def classe_entidade() -> type:
        return Lote

    def listar(self):
        nome_funcao = "listar"

        rotas = self.rotas(nome_funcao)
        self.limite.listar(self.exportar_entidades())

        opcao = self.limite.selecionar_opcao(nome_funcao)["menu"]
        retorno = self.selecione_rota(rotas, opcao, self.listar)

        if retorno is None:
            return self.entidades[self.LOTE_ENTIDADE]

        self.listar()

    def criar(self):
        nome_funcao = "criar"

        rotas = self.rotas(nome_funcao)
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao(nome_funcao)

        self.adicionar_entidade(self.LOTE_ENTIDADE, self.lista_para_lote(escolhas))

        self.selecione_rota(rotas, "v", self.listar)

    def deletar(self):
        nome_funcao = "deletar"

        rotas = self.rotas(nome_funcao)

        escolha = self.limite.selecionar_opcao(nome_funcao)["codigo_referencia"]
        self.remover_entidade(self.LOTE_ENTIDADE, self.entidades[self.LOTE_ENTIDADE].get(escolha))

        self.selecione_rota(rotas, "v", self.listar)

    def exportar_entidades(self) -> list:
        resp = []

        for chave in self.entidades[self.LOTE_ENTIDADE]:
            resp.append(self.entidades[self.LOTE_ENTIDADE][chave].objeto_limite())

        return resp

    @staticmethod
    def lista_para_lote(lista: dict) -> Lote:
        validacao_tipo(lista, dict)

        return Lote(
            lista["data_validade"],
            int(lista["quantidade"]),
        )
