from abc import ABC, abstractmethod


class LimiteAbstrato(ABC):
    CUSTOMIZACAO_CONSOLE = {
        "DEFAULT": "\033[0;0m",
        "LETRA_VERMELHA": "\033[31m",
        "LETRA_VERDE": "\033[32m",
        "LETRA_BRANCA": "\033[37m",
        "BACKGROUND_VERMELHA": "\033[41m",
    }

    def __init__(self, dado=None):
        self.dado = dado

    @staticmethod
    def classe_dado():
        return dict

    @abstractmethod
    def opcoes(self):
        pass

    def cabecalho(self):
        pass

    def roda_pe(self):
        pass

    def erro(self, mensagem):
        print("\n\n")
        print(self.CUSTOMIZACAO_CONSOLE["BACKGROUND_VERMELHA"])
        print("============================================================\n")
        print(self.CUSTOMIZACAO_CONSOLE["LETRA_BRANCA"])
        print("ERRO: \n\n  ", mensagem, "\n")
        print("============================================================")
        print(self.CUSTOMIZACAO_CONSOLE["DEFAULT"])
        print("\n\n")

    def listar(self, **filtros):
        raise Exception("Método [Listar] não permitido para este limite[%s]".format(self.__class__.__name__))

    def criar(self, **filtros):
        raise Exception("Método [Criar] não permitido para este limite[%s]".format(self.__class__.__name__))

    def atualizar(self, **filtros):
        raise Exception("Método [Atualizar] não permitido para este limite[%s]".format(self.__class__.__name__))

    def deletar(self, **filtros):
        raise Exception("Método [Deletar] não permitido para este limite[%s]".format(self.__class__.__name__))

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, dado):
        if isinstance(dado, self.classe_dado()) or dado is None:
            self.__dado = dado
            return

        raise Exception("Dado passado não é uma instancia de " + self.classe_dado().__name__)
