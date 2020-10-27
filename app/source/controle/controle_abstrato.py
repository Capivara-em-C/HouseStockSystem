from abc import ABC
from app.source.entidade.entidade_abstrata import EntidadeAbstrata
from app.source.limite.limite_abstrato import LimiteAbstrato
from app.source.exception.rotaInexistenteException import RotaInexistenteException
from app.source.helpers.setter import validacao_setter


class ControleAbstrato(ABC):
    def __init__(
            self,
            limite: LimiteAbstrato,
            entidade: EntidadeAbstrata or None = None
    ):
        self.limite = limite
        self.entidade = entidade

    def rotas(self, nome_funcao) -> dict:
        rota = {
            "listar": {
                "c": self.criar,
                "a": self.atualizar,
                "d": self.deletar,
                "v": self.voltar_listagem,
            },
            "criar": {
                "v": self.listar,
            },
            "atualizar": {
                "v": self.listar,
            },
            "show": {
                "v": self.listar
            }
        }

        try:
            return rota[nome_funcao]
        except KeyError:
            raise RotaInexistenteException("Rota passada não existente.")

    def selecione_opcao(self, rotas: dict, opcao: str, funcao):
        try:
            rotas[opcao]()
        except KeyError:
            self.limite.erro("Opção passada não existe, digite novamente.")
            funcao()

    @staticmethod
    def classe_limite():
        return LimiteAbstrato

    def listar(self, **filtros):
        raise Exception("Método [Listar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def criar(self, **filtros):
        raise Exception("Método [Criar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def atualizar(self, **filtros):
        raise Exception("Método [Atualizar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def deletar(self, **filtros):
        raise Exception("Método [Deletar] não permitido para este controle[%s]".format(self.__class__.__name__))

    def voltar_listagem(self):
        exit(0)

    @property
    def entidade(self):
        return self.__entidade

    @entidade.setter
    def entidade(self, entidade: EntidadeAbstrata or None = None):
        validacao_setter(entidade, self.classe_entidade())
        self.__entidade = entidade

    @staticmethod
    def classe_entidade():
        return EntidadeAbstrata

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite: LimiteAbstrato):
        validacao_setter(limite, self.classe_limite())
        self.__limite = limite
