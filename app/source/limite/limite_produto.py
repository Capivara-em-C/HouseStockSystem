from app.source.limite.limite_abstrato import LimiteAbstrato


class LimiteProduto(LimiteAbstrato):

    def opcoes(self) -> dict:
        return {
            "listar": {
                "menu": "Opções: \n" +
                " - Criar novo produto (c) \n" +
                " - Atualizar produto (a) \n" +
                " - Mostrar detalhes do produto (m) \n" +
                " - Deletar produto (d) \n" +
                " - Voltar (v) \n\n: ",
            },
            "criar": {
                "codigo_referencia": "Código de referência: ",
                "nome": "Nome: ",
                "descricao": "Descrição: ",
                "data_fabricacao": "Data de fabricação: ",
                "valor": "Valor: ",
                "prioridade": "Prioridade: ",
                "categoria": "Categoria: ",
                "estoque": "Quantidade em estoque: ",
                "estoque_minimo": "Estoque mínimo: ",
            },
            "atualizar": {
                "codigo_referencia": "Código de referência: ",
                "nome": "Nome: ",
                "descricao": "Descrição: ",
                "data_fabricacao": "Data de fabricação: ",
                "valor": "Valor: ",
                "prioridade": "Prioridade: ",
                "categoria": "Categoria: ",
                "estoque": "Quantidade em estoque: ",
                "estoque_minimo": "Estoque mínimo: ",
            },
            "mostrar": {
                "codigo_referencia": "Código de referência: "
            },
            "deletar": {
                "codigo_referencia": "Código de referência: "
            }
        }

    def listar(self, produtos: list or None = None):
        super().cabecalho()
        print("=================>  Listagem de produtos  <=================")
        self.cabecalho()

        if isinstance(produtos, list) and len(produtos) > 0:
            self.gerar_tabela(
                produtos,
                produtos[0].keys()
            )

        self.roda_pe()

    def criar(self):
        super().cabecalho()
        print("==================>  Criação de produto  <==================")
        self.cabecalho()

    def atualizar(self):
        super().cabecalho()
        print("==================>  Edição de produto   <==================")
        self.cabecalho()

    def mostrar(self, produto: dict):
        super().cabecalho()
        print("=================>  Detalhes de produtos  <================")
        self.cabecalho()

        if isinstance(produto, dict):
            for atributo in produto:
                print("{atributo}: {valor}".format(atributo=atributo, valor=produto.get(atributo)))

    def cabecalho(self):
        super().cabecalho()
        print("")
