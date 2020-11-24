from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_registro import ControleRegistro
from app.source.entidade.lote import Lote
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException
from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_lote import LimiteLote


class ControleLote(ControleAbstrato):
    @staticmethod
    def classe_limite() -> type:
        return LimiteLote

    @staticmethod
    def classe_entidade() -> type:
        return Lote

    def listar(self):
        try:
            nome_funcao = "listar"
            rotas = self.rotas(nome_funcao)
            self.limite.listar(self.exportar_entidades())
            opcao = self.limite.selecionar_opcao(nome_funcao)["menu"]
            retorno = self.selecione_rota(rotas, opcao, self.listar)

            if retorno is None:
                return self.entidades[self.LOTE_ENTIDADE]

            self.listar()
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

    def criar(self):
        try:
            nome_funcao = "criar"
            rotas = self.rotas(nome_funcao)
            self.limite.criar()
            escolhas = self.limite.selecionar_opcao(nome_funcao)
            self.adicionar_entidade(self.LOTE_ENTIDADE, self.lista_para_lote(escolhas))
            self.selecione_rota(rotas, "v", self.listar)
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
                TipoNaoCompativelException,
                CodigoReferenciaDuplicadoException,
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

    def deletar(self):
        try:
            nome_funcao = "deletar"
            rotas = self.rotas(nome_funcao)
            escolha = self.limite.selecionar_opcao(nome_funcao)["data_validade"]
            self.remover_entidade(self.LOTE_ENTIDADE, self.entidades[self.LOTE_ENTIDADE].get(escolha))
            self.selecione_rota(rotas, "v", self.listar)
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
                TipoNaoCompativelException,
                CodigoReferenciaDuplicadoException,
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

    def exportar_entidades(self) -> list:
        resp = []

        for chave in self.entidades[self.LOTE_ENTIDADE]:
            resp.append(self.entidades[self.LOTE_ENTIDADE][chave].objeto_limite())

        return resp

    @staticmethod
    def lista_para_lote(lista: dict) -> Lote:
        validacao_tipo(lista, dict)

        return Lote(
            lista["data_validade"],
            int(lista["quantidade"]),
        )
