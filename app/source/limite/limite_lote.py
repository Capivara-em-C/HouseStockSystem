from app.source.limite.limite_abstrato import LimiteAbstrato


class LimiteLote(LimiteAbstrato):
    @staticmethod
    def opcoes() -> dict:
        return {
            "listar": {
                "menu": "Opções: \n" +
                " - Criar novo lote (c) \n" +
                " - Deletar lote (d) \n" +
                " - Voltar (v) \n\n: ",
            },
            "criar": {
                "data_validade": "Data de validade: ",
                "quantidade": "Quantidade: ",
            },
            "deletar": {
                "data_validade": "Data de validade: ",
            },
        }

    def listar(self, lotes: list or None = None):
        super().cabecalho()
        print("=================>  Listagem de Lotes   <=================")
        self.cabecalho()

        if isinstance(lotes, list) and len(lotes) > 0:
            self.gerar_tabela(
                lotes,
                lotes[0].keys()
            )

        self.roda_pe()

    def criar(self):
        super().cabecalho()
        print("==================>  Criação de lote  <==================")
        self.cabecalho()

    def cabecalho(self):
        super().cabecalho()
        print("")
