from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.limite.limite_categoria import LimiteCategoria
from app.source.exception.rotaInexistenteException import RotaInexistenteException
from app.source.helpers.setter import validacao_tipo
from app.source.entidade.categoria import Categoria
from app.source.entidade.registro import Registro
from app.source.controle.controle_registro import ControleRegistro


class ControleCategoria(ControleAbstrato):
    @staticmethod
    def classe_limite() -> type:
        return LimiteCategoria

    def listar(self):
        nome_funcao = "listar"

        rotas = self.rotas(nome_funcao)
        self.limite.listar(self.exportar_entidades())

        opcao = self.limite.selecionar_opcao(nome_funcao)["menu"]

        ControleRegistro.adiciona_registro(
            "Moveu da Listagem de Categorias.",
            f"Requisição enviada pelo usuário:\n{opcao}"
        )

        retorno = self.selecione_rota(rotas, opcao, self.listar)

        if retorno is not None:
            self.listar()

    def criar(self):
        rotas = self.rotas("criar")
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao("criar")

        self.adicionar_entidade(self.CATEGORIA_ENTIDADE, self.lista_para_categoria(escolhas))

        ControleRegistro.adiciona_registro("Criou Categoria.", f"Requisição enviada pelo usuário:\n{escolhas}")

        self.selecione_rota(rotas, "v", self.listar)

    def atualizar(self):
        rotas = self.rotas("atualizar")
        self.limite.criar()
        escolhas = self.limite.selecionar_opcao("atualizar")

        registro_categoria = self.entidades[self.CATEGORIA_ENTIDADE]\
            .get(escolhas.get("codigo_referencia"))

        if registro_categoria is not None:
            registro_categoria = registro_categoria.objeto_limite()

        self.atualizar_entidade(self.CATEGORIA_ENTIDADE, self.lista_para_categoria(escolhas))

        ControleRegistro.adiciona_registro(
            "Atualizou categoria.",
            f"Requisição enviada pelo usuário:\n{escolhas}\n\nCategoria Antes da alteração:\n{registro_categoria}"
        )

        self.selecione_rota(rotas, "v", self.listar)

    def deletar(self):
        rotas = self.rotas("deletar")
        self.limite.criar()
        escolha = self.limite.selecionar_opcao("deletar")["codigo_referencia"]
        registro_categoria = self.entidades[self.CATEGORIA_ENTIDADE].get(escolha)

        if registro_categoria is not None:
            registro_categoria = registro_categoria.objeto_limite()

        self.remover_entidade(self.CATEGORIA_ENTIDADE, self.entidades[self.CATEGORIA_ENTIDADE].get(escolha))

        ControleRegistro.adiciona_registro(
            "Deletou categoria.",
            f"Requisição enviada pelo usuário:\n{escolha}\n\nCategoria deletada:\n{registro_categoria}"
        )

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
