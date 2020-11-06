from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_abstrato import LimiteAbstrato


class LimiteRegistro(LimiteAbstrato):
    @staticmethod
    def opcoes() -> dict:
        pass

    @staticmethod
    def listar(registros: list):
        validacao_tipo(registros, list)

        for registro in registros:
            print("============================================================")
            print(registro)
