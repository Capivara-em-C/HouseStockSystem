from abc import ABC

from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.entidade_nao_existente import EntidadeNaoExistente
from app.source.helpers.setter import validacao_tipo
from app.source.persistencia.DAO_abstrato import DAOAbstrato
from app.source.limite.limite_abstrato import LimiteAbstrato


class ControleAbstrato(ABC):
    # Lista de Entidades que salvas neste controle
    CATEGORIA_ENTIDADE = "categoria"
    LOTE_ENTIDADE = "lote"

    def __init__(self):
        self.limite = self.classe_limite()()

    def rotas(self, nome_funcao) -> dict:
        rota = {
            "listar": {
                "criar": self.criar,
                "editar": self.atualizar,
                "mostrar": self.mostrar,
                "apagar": self.deletar,
                self.limite.CANCEL: self.voltar_listagem,
            },
            "criar": {
                self.limite.CANCEL: self.listar,
            },
            "atualizar": {
                self.limite.CANCEL: self.listar,
            },
            "mostrar": {
                self.limite.CANCEL: self.listar,
            },
            "deletar": {
                self.limite.CANCEL: self.listar,
            }
        }

        rota_atual = rota.get(nome_funcao)

        if rota_atual is None:
            raise RotaInexistenteException("Rota passada não existente.")

        return rota_atual

    def selecione_rota(self, rotas: dict, opcao: str or None, funcao):
        rota = rotas.get(opcao)

        if rota is None:
            self.limite.erro("Opção passada não existe, digite novamente.")
            return funcao

        return rota

    def listar(self):
        raise MetodoNaoPermitidoException(self.metodo_nao_permitido_msg("Listar"))

    def criar(self):
        raise MetodoNaoPermitidoException(self.metodo_nao_permitido_msg("Criar"))

    def atualizar(self, identificador: str):
        raise MetodoNaoPermitidoException(self.metodo_nao_permitido_msg("Atualizar"))

    def mostrar(self, identificador: str):
        raise MetodoNaoPermitidoException(self.metodo_nao_permitido_msg("Mostrar"))

    def deletar(self, identificador: str):
        raise MetodoNaoPermitidoException()

    def metodo_nao_permitido_msg(self, metodo: str) -> str:
        return f"Método [{metodo}] não permitido para este controle[{self.__class__.__name__}]."

    def voltar_listagem(self) -> None:
        return None

    def exportar_entidades(self) -> list:
        resp = []

        for valor in self.entity_manager.get_all():
            resp.append(valor.objeto_limite())

        return resp

    @property
    def entidades(self) -> dict:
        return self.__entity_manager.get_all()

    @property
    def entity_manager(self):
        return self.__entity_manager

    @entity_manager.setter
    def entity_manager(self, entity_manager: DAOAbstrato):
        validacao_tipo(entity_manager, DAOAbstrato)
        self.__entity_manager = entity_manager

    def adicionar_entidade(self, entidade: EntidadeAbstrata):
        validacao_tipo(entidade, self.classe_entidade())

        if self.entity_manager.get_one_or_none(entidade.identificador) is not None:
            message = "O código de referência usado está duplicado, por favor insira um diferente."
            raise CodigoReferenciaDuplicadoException(message)

        self.entity_manager.add(entidade.identificador, entidade)

    def atualizar_entidade(self, entidade: EntidadeAbstrata, identificador: str or None = None):
        validacao_tipo(entidade, self.classe_entidade())

        if identificador is None:
            identificador = entidade.identificador

        validacao_tipo(identificador, str)

        if self.entity_manager.get(identificador) is None:
            raise EntidadeNaoExistente()

        if entidade.identificador != identificador and self.entity_manager.get_one_or_none(entidade.identificador):
            raise CodigoReferenciaDuplicadoException()

        self.entity_manager.remove(identificador)
        self.entity_manager.add(entidade.identificador, entidade)

        return self

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
