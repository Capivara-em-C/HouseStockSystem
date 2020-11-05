from abc import ABC, abstractmethod
from app.source.helpers.setter import validacao_tipo


class LimiteAbstrato(ABC):
    CUSTOMIZACAO_CONSOLE = {
        "DEFAULT": "\033[0;0m",
        "LETRA_VERMELHA": "\033[31m",
        "LETRA_VERDE": "\033[32m",
        "LETRA_BRANCA": "\033[37m",
        "BACKGROUND_VERMELHA": "\033[41m",
    }

    @staticmethod
    def classe_dado():
        return dict

    @abstractmethod
    def opcoes(self):
        pass

    def cabecalho(self):
        print("============================================================")

    def roda_pe(self):
        print("\n============================================================")

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

    def mostrar(self, **filtros):
        raise Exception("Método [Mostrar] não permitido para este limite[%s]".format(self.__class__.__name__))

    def deletar(self, **filtros):
        raise Exception("Método [Deletar] não permitido para este limite[%s]".format(self.__class__.__name__))

    def gerar_tabela(self, linhas: list, cabecalho: list or None = None):
        validacao_tipo(linhas, list)
        cabecalho = list(cabecalho)
        tamanho_colunas = self.tamanho_coluna(cabecalho, linhas)

        print(self.linha_formatada(cabecalho, tamanho_colunas))

        for linha in linhas:
            linha = list(linha.values())
            print(self.linha_formatada(linha, tamanho_colunas))

    @staticmethod
    def tamanho_coluna(cabecalho: list, lista_objeto_limite: list) -> dict:
        resp = {}
        margem = 4

        for coluna in cabecalho:
            resp[coluna] = len(coluna)

        for objeto_limite in lista_objeto_limite:
            for coluna in objeto_limite:
                tamanho_atual = len(str(objeto_limite[coluna]))

                if tamanho_atual > resp[coluna]:
                    resp[coluna] = tamanho_atual

        # Mais leve do que fazer as operações de soma/subtração em cada uma das rodadas
        # (podem haver centenas de registros, mas a quantidade de colunas será menor)
        for chave in resp:
            resp[chave] += margem

        return resp

    @staticmethod
    def linha_formatada(linha: list, tamanho_colunas: dict) -> str:
        linha_retorno = ""
        tamanho_colunas = list(tamanho_colunas.values())

        cont = 0
        for coluna in linha:
            tamanho_coluna = tamanho_colunas[cont]
            str_coluna = str(coluna)
            cont += 1

            tamanho_coluna -= len(str_coluna)
            espacos_esquerda = tamanho_coluna // 2

            margem_esquerda = " " * espacos_esquerda
            margem_direita = " " * (tamanho_coluna - espacos_esquerda)

            linha_retorno += margem_esquerda + str(coluna) + margem_direita

            if linha.index(coluna) != len(linha) - 1:
                linha_retorno += "|"

        return linha_retorno

    def selecionar_opcao(self):
        selecionados = []
        for opcao in self.opcoes():
            selecionados += [input(opcao)]

        return selecionados
