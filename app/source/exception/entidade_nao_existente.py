class EntidadeNaoExistente(Exception):
    def __init__(self, message: str = None):
        if message is None:
            message = "A entidade informada não existe.\n"
            message += "Por favor inserte outro identificador."

        super().__init__(message)