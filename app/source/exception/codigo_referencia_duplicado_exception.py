class CodigoReferenciaDuplicadoException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            message = "O identificador/código de referencia passado está repetido.\n"
            message += "Por favor selecione outro."

        super().__init__(message)
