import PySimpleGUI as Sg

from app.source.helpers.setter import validacao_tipo


class LimiteAbstrato:
    CANCEL = "Cancelar"
    SUBMIT = "Salvar"

    def __init__(self, titulo: str = ""):
        validacao_tipo(titulo, str)

        self.__titulo = titulo
        self.layout = []

    def addRowToLayout(self, row: list):
        validacao_tipo(row, list)
        self.layout.append(row)

    def add_default_buttons(self):
        self.addRowToLayout([
            Sg.Submit(button_text=self.SUBMIT, key=self.CANCEL),
            Sg.Cancel(button_text=self.CANCEL, key=self.SUBMIT)
        ])

    def window(self, titulo: str = "", tamanho: tuple or None = None):
        layout = self.layout

        if titulo == "":
            titulo = self.__titulo

        if tamanho is not None:
            layout = [[Sg.Column(self.layout, size=tamanho, scrollable=True, vertical_scroll_only=True)]]

        window = Sg.Window(title=titulo).Layout(rows=layout)
        button, values = window.Read()
        window.close()

        self.layout = []

        if button == self.CANCEL:
            return None

        return {"botao": button, "valores": values}

    def gerar_tabela(
            self,
            valores: list,
            tamanho_coluna: list,
            cabecalho: list or None = None,
            tooltip: str = "",
            chave: str or None = None
    ):
        validacao_tipo(valores, list)
        validacao_tipo(tamanho_coluna, list)
        validacao_tipo(tooltip, str)

        if cabecalho is not None:
            validacao_tipo(cabecalho, list)

        if chave is None:
            chave = "tabela"

        validacao_tipo(chave, str)

        self.addRowToLayout([Sg.Table(
            values=valores,
            justification='center',
            key=chave,
            headings=cabecalho,
            bind_return_key=True,
            tooltip=tooltip,
            col_widths=tamanho_coluna,
            size=(500, 50),
            display_row_numbers=True,
            num_rows=20,
            select_mode=Sg.SELECT_MODE_BROWSE
        )])

    def erro(self, message: str = ""):
        self.layout = []

        if message == "":
            message = "Um erro inesperado aconteceu."

        self.addRowToLayout([
            Sg.Text(text=message, text_color="red")
        ])

        self.window("ERRO")

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, layout: list):
        validacao_tipo(layout, list)
        self.__layout = layout
