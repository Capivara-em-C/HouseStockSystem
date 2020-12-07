from app.source.limite.limite_abstrato import LimiteAbstrato, Sg


class LimiteInicio(LimiteAbstrato):
    def __init__(self):
        super().__init__("Home")

    def home(self):
        self.addRowToLayout([
            Sg.SimpleButton(button_text="Listagem de Produtos", key="produtos", size=(18, 8)),
            Sg.Text(size=(1, 2)),
            Sg.SimpleButton(button_text="Listagem de Categorias", key="categorias", size=(18, 8)),
        ])

        self.addRowToLayout([
            Sg.SimpleButton("Registros", key="registros", size=(41, 8))
        ])

        return self.window()
