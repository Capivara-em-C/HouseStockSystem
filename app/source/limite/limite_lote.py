from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_abstrato import LimiteAbstrato, Sg


class LimiteLote(LimiteAbstrato):
    CANCEL = "Voltar"

    def __init__(self):
        super().__init__("Lotes")

    def listar(self, lotes: list or None = None):
        if lotes is None or not lotes:
            lotes = [["", "", "", ]]

        validacao_tipo(lotes, list)

        self.gerar_tabela(
            valores=lotes,
            tamanho_coluna=[20, 20],
            cabecalho=["Data de validade", "Quantidade"],
            tooltip="Clique duas vezes em uma das linhas para selecionar uma ação.",
        )

        self.addRowToLayout([
            Sg.Cancel(button_text=self.CANCEL),
            Sg.Button(button_text="Criar", key="criar")
        ])

        return self.window()

    def criar(self):
        self.__formulario()

        self.addRowToLayout([
            Sg.Cancel(button_text=self.CANCEL),
            Sg.Button(button_text="Criar", key="criar")
        ])

        return self.window()

    def atualizar(self, lote: dict):
        validacao_tipo(propriedade=lote, tipo=dict)

        self.__formulario(lote)

        self.addRowToLayout([
            Sg.Cancel(button_text=self.CANCEL),
            Sg.Button(button_text="Atualizar", key="atualizar")
        ])

        return self.window()

    def tabela_opcoes(self):
        self.addRowToLayout([
            Sg.SimpleButton(button_text="Editar", key="editar", size=(10, 8)),
            Sg.SimpleButton(button_text="Apagar", key="apagar", size=(10, 8)),
        ])

        return self.window()

    def __formulario(self, lote: dict or None = None):
        if lote is None:
            lote = {}

        validacao_tipo(propriedade=lote, tipo=dict)

        self.addRowToLayout([
            Sg.Text(text="Data de validade: "),
            Sg.InputText(key="data_validade", default_text=lote.get("data_validade"))
        ])

        self.addRowToLayout([
            Sg.Text(text="Quantidade: "),
            Sg.InputText(key="quantidade", default_text=lote.get("quantidade"))
        ])
