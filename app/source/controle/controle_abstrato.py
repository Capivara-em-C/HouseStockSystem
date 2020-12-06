from abc import ABC

from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.entidade_nao_existente import EntidadeNaoExistente
from app.source.helpers.setter import validacao_tipo
from app.source.limite_console.limite_abstrato import LimiteAbstrato
from app.source.persistencia.DAO_abstrato import DAOabstrato


class ControleAbstrato(ABC):
    # Lista de Entidades que salvas neste controle
    PRODUTO_ENTIDADE = "produtos"
    CATEGORIA_ENTIDADE = "categoria"
    LOTE_ENTIDADE = "lote"

    def __init__(
            self,
            limite: LimiteAbstrato or None = None
    ):
        if limite is None:
            limite = self.classe_limite()()

        self.limite = limite
        self.entidades = DAOabstrato()

    def rotas(self, nome_funcao) -> dict:
        rota = {
            "listar": {
                "c": self.criar,
                "a": self.atualizar,
                "m": self.mostrar,
                "d": self.deletar,
                "v": self.voltar_listagem,
            },
            "criar": {
                "v": self.listar,
            },
            "atualizar": {
                "v": self.listar,
            },
            "mostrar": {
                "v": self.listar
            },
            "deletar": {
                "v": self.listar
            }
        }

        rota_atual = rota.get(nome_funcao)

        if rota_atual is None:
            raise RotaInexistenteException("Rota passada não existente.")

        return rota_atual

    def selecione_rota(self, rotas: dict, opcao: str, funcao):
        rota = rotas.get(opcao)

        if rota is None:
            self.limite.erro("Opção passada não existe, digite novamente.")
            funcao()
            return

        rota()

    def listar(self):
        raise MetodoNaoPermitidoException(self.metodo_nao_permitido_msg("Listar"))

    def criar(self):
        raise MetodoNaoPermitidoException(self.metodo_nao_permitido_msg("Criar"))

    def atualizar(self):
        raise MetodoNaoPermitidoException(self.metodo_nao_permitido_msg("Atualizar"))

    def mostrar(self):
        raise MetodoNaoPermitidoException(self.metodo_nao_permitido_msg("Mostrar"))

    def deletar(self):
        raise MetodoNaoPermitidoException()

    def metodo_nao_permitido_msg(self, metodo: str) -> str:
        return f"Método [{metodo}] não permitido para este controle[{self.__class__.__name__}]."

    def voltar_listagem(self) -> None:
        return None

    def exportar_entidades(self) -> list:
        resp = []

        for valor in self.entidades.get_all():
            resp.append(valor.objeto_limite())

        return resp

    @property
    def entidades(self) -> dict:
        return self.__entidades.get_all()

    def adicionar_entidade(self, tipo_entidade: str, entidade: EntidadeAbstrata):
        validacao_tipo(tipo_entidade, str)
        validacao_tipo(entidade, self.classe_entidade())

        if self.entidades.get(entidade.identificador) is not None:
            message = "O código de referência usado está duplicado, por favor insira um diferente."
            raise CodigoReferenciaDuplicadoException(message)

        self.entidades.add(entidade.identificador, entidade)

    def atualizar_entidade(self,identificador , entidade: EntidadeAbstrata):
        validacao_tipo(entidade, self.classe_entidade())

        # @TODO make soft to only update variables that user really want
        if self.entidades.get(identificador) is None:
            raise EntidadeNaoExistente()

        self.entidades.remove(identificador)
        self.entidades.add(identificador, entidade)

    def remover_entidade(self, identificador):
        self.entidades.remove(identificador)

    @staticmethod
    def classe_entidade() -> type:
        return EntidadeAbstrata

    @property
    def limite(self) -> LimiteAbstrato:
        return self.__limite

    @limite.setter
    def limite(self, limite: LimiteAbstrato):
        validacao_tipo(limite, self.classe_limite())
        self.__limite = limite

    @staticmethod
    def classe_limite() -> type:
        return LimiteAbstrato
