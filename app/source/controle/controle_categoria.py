from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.limite.limite_categoria import LimiteCategoria
from app.source.exception.rotaInexistenteException import RotaInexistenteException
from app.source.helpers.setter import validacao_tipo
from app.source.entidade.categoria import Categoria
from app.source.entidade.registro import Registro
from app.source.controle.controle_registro import ControleRegistro
from datetime import datetime



class ControleCategoria(ControleAbstrato):

    @staticmethod
    def classe_limite() -> type:
        return LimiteCategoria

    def listar(self):
        nome_funcao = "listar"

        rotas = self.rotas(nome_funcao)
        self.limite.listar(self.exportar_entidades())

        opcao = self.limite.selecionar_opcao(nome_funcao)["menu"]
        retorno = self.selecione_rota(rotas, opcao, self.listar)

        if retorno is not None:
            self.listar()

    def criar(self):
        rotas = self.rotas("criar")
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao("criar")

        self.adicionar_entidade(self.CATEGORIA_ENTIDADE, self.lista_para_categoria(escolhas))

        hora = datetime.now()
        ControleRegistro.adiciona_registro("Criou categoria as: ", str(hora))

        self.selecione_rota(rotas, "v", self.listar)

    def atualizar(self):
        rotas = self.rotas("atualizar")
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao("atualizar")

        self.atualizar_entidade(self.CATEGORIA_ENTIDADE, self.lista_para_categoria(escolhas))

        hora = datetime.now()
        ControleRegistro.adiciona_registro("Atualizou categoria as: ", str(hora))

        self.selecione_rota(rotas, "v", self.listar)

    def deletar(self):
        rotas = self.rotas("deletar")
        self.limite.criar()
        escolha = self.limite.selecionar_opcao("deletar")["codigo_referencia"]

        self.remover_entidade(self.CATEGORIA_ENTIDADE, self.entidades[self.CATEGORIA_ENTIDADE].get(escolha))

        hora = datetime.now()
        ControleRegistro.adiciona_registro("Deletou categoria as: ", str(hora))

        self.selecione_rota(rotas, "v", self.listar)

    def voltar_listagem(self) -> None:
        return None

    @staticmethod
    def lista_para_categoria(lista: dict) -> Categoria:
        validacao_tipo(lista, dict)

        return Categoria(
            lista["codigo_referencia"],
            lista["nome"],
        )

    def exportar_entidades(self) -> list:
        resp = []

        for chave in self.entidades[self.CATEGORIA_ENTIDADE]:
            resp.append(self.entidades[self.CATEGORIA_ENTIDADE][chave].objeto_limite())

        return resp
