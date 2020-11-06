from app.source.entidade.registro import Registro
from app.source.controle.controle_abstrato import ControleAbstrato


class ControleRegistro(ControleAbstrato):

    global registros
    registros = []

    @staticmethod
    def adiciona_registro(acao: str, hora: str):
        registros.append(Registro(acao, hora))

    @staticmethod
    def mostra_registros() -> list:
        resp = []

        for registro in registros:
            resp.append(registro.acao + registro.hora)

        return resp