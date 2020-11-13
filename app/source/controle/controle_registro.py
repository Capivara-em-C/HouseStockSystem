from traceback import format_exc

from app.source.entidade.registro import Registro
from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException
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
        try:
            self.limite.listar(self.mostra_registros())

            self.adiciona_registro(
                "Visualizou os registros.",
                ""
            )
        except (
            RotaInexistenteException,
            TipoNaoCompativelException,
            CodigoReferenciaDuplicadoException
        ) as err:
            self.limite.erro(err)
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except ValueError as err:
            self.limite.erro(
                "Algum argumento passado foi do tipo errado[Número ou palavra]\n" +
                "(Exemplo: No cadastro de um produto você passou uma letra para o valor)."
            )
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except Exception as err:
            self.limite.erro("Erro inesperado ocorreu!")
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())

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
