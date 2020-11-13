from abc import ABC
from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.limite.limite_abstrato import LimiteAbstrato
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.helpers.setter import validacao_tipo


class ControleAbstrato(ABC):
    # Lista de Entidades que salvas neste controle
    PRODUTO_ENTIDADE = "produtos"
    CATEGORIA_ENTIDADE = "categoria"
    LOTE_ENTIDADE = "lote"

    def __init__(
            self,
            limite: LimiteAbstrato or None = None,
            entidades: dict or None = None
    ):
        if limite is None:
            limite = self.classe_limite()()

        self.limite = limite
        self.entidades = entidades

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
        rota = rotas[opcao]

        if rota is None:
            self.limite.erro("Opção passada não existe, digite novamente.")
            funcao()
            return

        rota()

    def listar(self):
        raise Exception("Método [Listar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def criar(self):
        raise Exception("Método [Criar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def atualizar(self):
        raise Exception("Método [Atualizar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def mostrar(self):
        raise Exception("Método [Mostrar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def deletar(self):
        raise Exception("Método [Deletar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def voltar_listagem(self) -> None:
        return None

    def exportar_entidades(self) -> list:
        resp = []

        for chave in self.entidades[self.PRODUTO_ENTIDADE]:
            resp.append(self.entidades[self.PRODUTO_ENTIDADE][chave].objeto_limite())

        return resp

    @property
    def entidades(self) -> dict:
        return self.__entidades

    @entidades.setter
    def entidades(self, listas_entidades: dict or None = None):
        if listas_entidades is None:
            listas_entidades = {
                self.PRODUTO_ENTIDADE: {},
                self.CATEGORIA_ENTIDADE: {},
                self.LOTE_ENTIDADE: {},
            }

        validacao_tipo(listas_entidades, dict)

        for entidades in listas_entidades.values():
            if entidades is not None:
                validacao_tipo(entidades, dict)

                if entidades.get(self.PRODUTO_ENTIDADE):
                    validacao_tipo(entidades, self.classe_entidade())

        self.__entidades = listas_entidades

    def adicionar_entidade(self, tipo_entidade: str, entidade: EntidadeAbstrata):
        validacao_tipo(tipo_entidade, str)
        validacao_tipo(entidade, self.classe_entidade())

        if self.entidades[tipo_entidade].get(entidade.identificador) is not None:
            raise CodigoReferenciaDuplicadoException

        self.entidades[tipo_entidade][entidade.identificador] = entidade

    def atualizar_entidade(self, tipo_entidade: str, entidade: EntidadeAbstrata):
        validacao_tipo(tipo_entidade, str)
        validacao_tipo(entidade, self.classe_entidade())

        # @TODO make soft to only update variables that user really want
        self.entidades[tipo_entidade][entidade.identificador] = entidade

    def remover_entidade(self, tipo_entidade: str, entidade: EntidadeAbstrata or None):
        validacao_tipo(tipo_entidade, str)

        if entidade is None:
            return self

        validacao_tipo(entidade, self.classe_entidade())
        tipo = self.entidades.get(tipo_entidade)

        if tipo is None or tipo.get(entidade.identificador) is None:
            return self

        del(self.entidades[tipo_entidade][entidade.identificador])

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
