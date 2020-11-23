class MetodoNaoPermitidoException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            message = "Método/opção passado(a) não permitido(a).\n"
            message += "Por favor selecione outro."

        super().__init__(message)
