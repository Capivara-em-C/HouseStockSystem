from app.source.limite.limite_abstrato import LimiteAbstrato


class LimiteProduto(LimiteAbstrato):

    def opcoes(self) -> dict:
        return {
            "listar": {
                "menu": "Opções: \n" +
                " - Criar novo produto (c) \n" +
                " - Editar produto (e) \n" +
                " - Detalhes do produto (d) \n" +
                " - Apagar produto (a) \n" +
                " - Voltar (v) \n\n",
            },
            "criar": {
                "codigo_referencia": "Digite as informações requeridas: \n" +
                "Código de referência: ",
                "nome": "Nome: ",
                "descricao": "Descrição: ",
                "data_fabricacao": "Data de fabricação: ",
                "valor": "Valor: ",
                "prioridade": "Prioridade: ",
                "estoque": "Quantidade em estoque: ",
                "estoque_minimo": "Estoque mínimo: ",
            },
        }

    def listar(self, produtos: list or None = None):
        self.cabecalho()

        if isinstance(produtos, list) and len(produtos) > 0:
            self.gerar_tabela(
                produtos,
                produtos[0].keys()
            )

        self.roda_pe()

    def cabecalho(self):
        super().cabecalho()
        print("=================>  Listagem de produtos  <=================")
        super().cabecalho()
        print("")

    def criar(self):
        pass
