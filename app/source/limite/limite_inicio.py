from app.source.limite.limite_abstrato import LimiteAbstrato


class LimiteInicio(LimiteAbstrato):
    def cabecalho(self):
        print("============================================================\n")
        print("                           Home                             \n")
        print("------------------------------------------------------------\n")

    def roda_pe(self):
        print("============================================================\n")

    def home(self):
        self.cabecalho()
        print("                    Seja bem vindo *u*!                     \n")
        self.roda_pe()

    def opcoes(self):
        return [
            "Opções: \n" +
            " - Adicionar quantidade a um item (a) \n" +
            " - Remover quantidade de um item (r) \n" +
            " - Listagem de Produtos (p) \n" +
            " - Sair (s) \n\n",
        ]

    def selecionar_opcao(self):
        selecionados = []
        for opcao in self.opcoes():
            selecionados += [input(opcao)]

        self.roda_pe()
        return selecionados