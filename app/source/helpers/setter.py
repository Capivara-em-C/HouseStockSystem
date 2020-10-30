from app.source.exception.tipoNaoCompativelException import TipoNaoCompativelException


def validacao_tipo(propriedade, tipo):
    if not isinstance(propriedade, tipo):
        raise TipoNaoCompativelException(
            "Propriedade passada[" + str(propriedade) + "] " + " não é um do tipo[ " + tipo.__name__ + "]."
        )