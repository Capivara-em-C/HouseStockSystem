from app.source.limite_console.limite_abstrato import LimiteAbstrato


class LimiteCategoria(LimiteAbstrato):

    def opcoes(self) -> dict:
        return {
            "listar": {
                "menu": "Opções: \n" +
                " - Criar nova categoria (c) \n" +
                " - Atualizar categoria (a) \n" +
                " - Deletar categoria (d) \n" +
                " - Voltar (v) \n\n",
            },
            "criar": {
                "codigo_referencia": "Código de referência: ",
                "nome": "Nome: ",

            },
            "atualizar": {
                "codigo_referencia": "Código de referência: ",
                "nome": "Nome: ",

            },
            "deletar": {
                "codigo_referencia": "Código de referência: "
            }
        }

    def listar(self, categorias: list or None = None):
        self.cabecalho()

        if isinstance(categorias, list) and len(categorias) > 0:
            self.gerar_tabela(
                categorias,
                categorias[0].keys()
            )

        self.roda_pe()

    def cabecalho(self):
        super().cabecalho()
        print("================> Listagem de Categorias <================")
        super().cabecalho()
        print("")

    def criar(self):
        pass
