from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_categoria import ControleCategoria
from app.source.controle.controle_produto import ControleProduto
from app.source.controle.controle_registro import ControleRegistro
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.limite.limite_categoria import LimiteCategoria
from app.source.limite.limite_inicio import LimiteInicio
from app.source.limite.limite_produto import LimiteProduto
from app.source.limite.limite_registro import LimiteRegistro


class ControleInicio(ControleAbstrato):
    @staticmethod
    def classe_limite():
        return LimiteInicio

    def rotas(self, nome_funcao):
        rota = {
            "home": {
                "p": self.produto,
                "c": self.categoria,
                "r": self.registros,
                "s": exit
            },
        }

        try:
            return rota[nome_funcao]
        except KeyError:
            raise RotaInexistenteException("Rota passada não existente.")

    def home(self):
        try:
            rotas = self.rotas("home")
            self.limite.home()
            opcao = self.limite.selecionar_opcao("home")["menu"]

            ControleRegistro.adiciona_registro(
                "Moveu da Home.",
                f"Requisição enviada pelo usuário:\n{opcao}"
            )

            self.selecione_rota(rotas, opcao, self.home)
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
            controle_produto = ControleProduto(LimiteProduto())
            controle_produto.entidades = self.entidades
            controle_produto.listar()
            self.entidades = controle_produto.entidades
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
            controle_categoria = ControleCategoria(LimiteCategoria())
            controle_categoria.entidades = self.entidades
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
            ControleRegistro(LimiteRegistro()).Listar()
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
