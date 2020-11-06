from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException


def validacao_tipo(propriedade, tipo: type):
    if not isinstance(propriedade, tipo):
        raise TipoNaoCompativelException(
            "Propriedade passada[" + propriedade.__class__.__name__ + "] " + " não é um do tipo[ " + tipo.__name__ + "]."
        )

def validacao_multipla_tipo_e(propriedade, tipos: list):
    validacao_tipo(tipos, list)

    for tipo in tipos:
        validacao_tipo(propriedade, tipo)


def validacao_multipla_tipo_ou(propriedade, tipos: list):
    validacao_tipo(tipos, list)
    validacao = False

    for tipo in tipos:
        validacao |= (tipo is None and propriedade is None) or isinstance(propriedade, tipo)

    if not validacao:
        raise TipoNaoCompativelException(
            "Propriedade passada[" + str(propriedade) + "] " +
            " não é um dos tipos[ " + str(tipos) + "]."
        )
