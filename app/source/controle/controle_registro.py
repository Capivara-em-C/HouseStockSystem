from app.source.entidade.registro import Registro
from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.limite.limite_registro import LimiteRegistro
from app.source.helpers.setter import validacao_tipo


class ControleRegistro(ControleAbstrato):
    global registros
    registros = []

    @staticmethod
    def classe_limite():
        return LimiteRegistro

    @staticmethod
    def adiciona_registro(titulo: str, requisicao: str):
        validacao_tipo(titulo, str)
        validacao_tipo(requisicao, str)
        registros.append(Registro(titulo, requisicao))

    def Listar(self):
        self.limite.listar(self.mostra_registros())

        self.adiciona_registro(
            "Visualizou os registros.",
            ""
        )


    @staticmethod
    def mostra_registros() -> list:
        resp = []

        for registro in registros:
            resp.append(
                f"[{registro.hora}] {registro.titulo}\n" +
                "------------------------------------------------------------\n" +
                f"{registro.requisicao}"
            )

        return resp
