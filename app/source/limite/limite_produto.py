from app.source.helpers.setter import validacao_tipo, validacao_multipla_tipo_ou
from app.source.limite.limite_abstrato import LimiteAbstrato, Sg


class LimiteProduto(LimiteAbstrato):
    CANCEL = "Voltar"

    def __init__(self):
        super().__init__("Voltar")

    def listar(self, produtos: list or None = None):
        validacao_multipla_tipo_ou(produtos, (list, None))

        if produtos is None or produtos == list():
            produtos = [["", "", "", ]]

        self.gerar_tabela(
            valores=produtos,
            tamanho_coluna=[20, 20, 20],
            cabecalho=["Nº Referencia", "Nome", "Quantidade"],
            tooltip="Clique duas vezes em uma das linhas para selecionar uma ação.",
        )

        self.addRowToLayout([
            Sg.Cancel(button_text=self.CANCEL),
            Sg.Button(button_text="Criar", key="criar")
        ])

        return self.window()

    def tabela_opcoes(self):
        self.addRowToLayout([
            Sg.SimpleButton(button_text="Mostrar", key="mostrar", size=(10, 8)),
            Sg.SimpleButton(button_text="Editar", key="editar", size=(10, 8)),
            Sg.SimpleButton(button_text="Apagar", key="apagar", size=(10, 8)),
        ])

        return self.window()

    def criar(self):
        self.__formulario()

        return self.window()

    def atualizar(self, produto: dict):
        self.__formulario(produto)

        return self.window()

    def __formulario(self, produto: dict or None = None):
        if produto is None:
            produto = {}

        validacao_tipo(propriedade=produto, tipo=dict)

        self.addRowToLayout([
            Sg.Text(text="Código de referência: "),
            Sg.InputText(key="codigo", default_text=produto.get("identificador"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Nome: "),
            Sg.InputText(key="nome", default_text=produto.get("nome"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Descrição: "),
            Sg.InputText(key="descricao", default_text=produto.get("descricao"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Data de fabricacao: "),
            Sg.InputText(key="data_fabricacao", default_text=produto.get("data_fabricacao"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Valor: "),
            Sg.InputText(key="valor", default_text=produto.get("valor"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Prioridade: "),
            Sg.InputText(key="prioridade", default_text=produto.get("prioridade"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Estoque: "),
            Sg.InputText(key="estoque", default_text=produto.get("estoque"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Estoque mínimo: "),
            Sg.InputText(key="estoque_minimo", default_text=produto.get("estoque_minimo"))
        ])

        self.relacionamento_categoria(produto.get("categorias"))
        self.relacionamento_lote(produto.get("lotes"))

    def relacionamento_categoria(self, categorias: list or None = None):
        if categorias is None:
            categorias = [
                ["", "", ],
            ]

        validacao_tipo(categorias, list)

        self.gerar_tabela(
            valores=categorias,
            tamanho_coluna=[20, 20, ],
            cabecalho=["Código de referência", "Nome"],
            tooltip="Clique duas vezes em uma das linhas para selecionar uma ação.",
            chave="categorias",
        )

    def relacionamento_lote(self, lotes: list or None = None):
        if lotes is None:
            lotes = [
                ["", "", ],
            ]

        validacao_tipo(lotes, list)

        self.gerar_tabela(
            valores=lotes,
            tamanho_coluna=[20, 20, ],
            cabecalho=["Data de Validade", "Quantidade"],
            tooltip="Clique duas vezes em uma das linhas para selecionar uma ação.",
            chave="lotes",
        )
