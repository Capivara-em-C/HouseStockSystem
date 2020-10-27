from app.source.exception.tipoNaoCompativelException import TipoNaoCompativelException


def validacao_setter(propriedade, tipo):
    if not isinstance(propriedade, tipo):
        raise TipoNaoCompativelException(
            "Propriedade passada[" + str(propriedade) + "] " + " não é um do tipo[ " + tipo.__name__ + "]."
        )