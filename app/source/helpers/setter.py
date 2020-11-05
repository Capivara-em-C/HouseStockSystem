from app.source.exception.tipoNaoCompativelException import TipoNaoCompativelException


def validacao_tipo(propriedade, tipo: type):
    if isinstance(tipo, list):
        for tipo_interno in tipo:
            validacao_tipo(propriedade, tipo_interno)

    if not isinstance(propriedade, tipo):
        raise TipoNaoCompativelException(
            "Propriedade passada[" + str(propriedade) + "] " + " não é um do tipo[ " + tipo.__name__ + "]."
        )


def validacao_multipla_tipo_ou(propriedade, tipos):
    if isinstance(tipos, list) or isinstance(tipos, dict):
        for tipo_interno in tipos:
            validacao_tipo(propriedade, tipo_interno)
