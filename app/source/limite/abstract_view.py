import PySimpleGUI as Sg
from app.source.helpers.setter import validacao_tipo


class AbstractView:
    CANCEL = "Cancelar"
    SUBMIT = "Salvar"

    def __init__(self, titulo: str = ""):
        validacao_tipo(titulo, str)

        self.__titulo = titulo
        self.layout = []

    def addRowToLayout(self, row):
        self.layout.append(row)

    def add_default_buttons(self):
        self.addRowToLayout([
            Sg.Submit(button_text=self.SUBMIT, key="action"),
            Sg.Cancel(button_text=self.CANCEL, key="action")
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

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, layout: list):
        validacao_tipo(layout, list)
        self.__layout = layout
