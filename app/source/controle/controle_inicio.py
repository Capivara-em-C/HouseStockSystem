from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_categoria import ControleCategoria
from app.source.controle.controle_produto import ControleProduto
from app.source.controle.controle_registro import ControleRegistro
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.limite.limite_inicio import LimiteInicio


class ControleInicio(ControleAbstrato):
    @staticmethod
    def classe_limite():
        return LimiteInicio

    def rotas(self, nome_funcao):
        rota = {
            "home": {
                "produtos": self.produto,
                "categorias": self.categoria,
                "registros": self.registros,
                None: exit
            },
        }

        try:
            return rota[nome_funcao]
        except KeyError:
            raise RotaInexistenteException("Rota passada não existente.")

    def home(self):
        try:
            rotas = self.rotas("home")
            opcao = self.limite.home()

            ControleRegistro.adiciona_registro(
                "Moveu da Home.",
                f"Requisição enviada pelo usuário:\n{opcao.get('botao')}"
            )

            self.selecione_rota(rotas, opcao.get('botao'), self.home)()
            self.home()
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
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

    def produto(self):
        try:
            controle_produto = ControleProduto()
            controle_produto.listar()
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
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

    def categoria(self):
        try:
            controle_categoria = ControleCategoria(self.entidades)
            controle_categoria.listar()
            self.entidades = controle_categoria.entidades
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
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

    def registros(self):
        try:
            ControleRegistro().Listar()
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
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
