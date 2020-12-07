from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_abstrato import LimiteAbstrato, Sg


class LimiteCategoria(LimiteAbstrato):
    CANCEL = "Voltar"

    def __init__(self):
        super().__init__("Voltar")

    def listar(self, categorias: list or None = None):
        if categorias is None or not categorias:
            categorias = [["", "", ]]

        validacao_tipo(categorias, list)

        self.gerar_tabela(
            valores=categorias,
            tamanho_coluna=[20, 20, ],
            cabecalho=["Nº Referencia", "Nome", ],
            tooltip="Clique duas vezes em uma das linhas para selecionar uma ação.",
        )

        self.addRowToLayout([
            Sg.Cancel(button_text=self.CANCEL),
            Sg.Button(button_text="Criar", key="criar")
        ])

        return self.window()

    def tabela_opcoes(self):
        self.addRowToLayout([
            Sg.SimpleButton(button_text="Editar", key="editar", size=(10, 8)),
            Sg.SimpleButton(button_text="Apagar", key="apagar", size=(10, 8)),
        ])

        return self.window()

    def criar(self):
        self.__formulario()

        self.addRowToLayout([
            Sg.Cancel(button_text=self.CANCEL),
            Sg.Button(button_text="Criar", key="criar")
        ])

        return self.window()

    def atualizar(self, categoria: dict):
        validacao_tipo(propriedade=categoria, tipo=dict)

        self.__formulario(categoria)

        self.addRowToLayout([
            Sg.Cancel(button_text=self.CANCEL),
            Sg.Button(button_text="Atualizar", key="atualizar")
        ])

        return self.window()

    def __formulario(self, categoria: dict or None = None):
        if categoria is None:
            categoria = {}

        validacao_tipo(propriedade=categoria, tipo=dict)

        self.addRowToLayout([
            Sg.Text(text="Código de referência: "),
            Sg.InputText(key="identificador", default_text=categoria.get("identificador"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Nome: "),
            Sg.InputText(key="nome", default_text=categoria.get("nome"))
        ])
