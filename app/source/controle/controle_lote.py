from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_registro import ControleRegistro
from app.source.entidade.lote import Lote
from app.source.entidade.produto_perecivel import ProdutoPerecivel
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.entidade_nao_existente import EntidadeNaoExistente
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException
from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_lote import LimiteLote
from app.source.persistencia.DAO_produto import DAOProduto


class ControleLote(ControleAbstrato):
    def __init__(self, produto: ProdutoPerecivel):
        super().__init__()
        self.__produto = produto
        self.entity_manager = DAOProduto()

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
            requisicao = self.limite.listar(self.exportar_entidades())
            botao = requisicao.get('botao')

            if botao is None:
                return

            valores = requisicao.get("valores")
            identificador = ""

            if valores and isinstance(valores, dict) and botao == 'tabela':
                identificador = valores.get("tabela")
                if identificador and isinstance(identificador, list) and len(identificador) > 0:
                    lotes = list(self.__produto.lotes.values())
                    identificador = lotes[identificador[0]].identificador
                else:
                    self.listar()
                    return

            if botao == 'tabela':
                botao = self.limite.tabela_opcoes().get('botao')

                if botao is None:
                    self.listar()
                    return

            if botao in ("editar", "apagar"):
                retorno = self.selecione_rota(rotas, botao, self.listar)(identificador)
            else:
                retorno = self.selecione_rota(rotas, botao, self.listar)()

            if retorno is not None:
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
            requisicao = self.limite.criar()

            botao = requisicao.get("botao")
            valores = requisicao.get("valores")

            if botao is None:
                self.listar()
                return

            if self.__produto.lotes.get(valores.get("data_validade")):
                raise CodigoReferenciaDuplicadoException()

            self.__produto.add_lote(Lote(
                valores.get("data_validade"),
                int(valores.get("quantidade")),
            ))

            self.listar()
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

    def atualizar(self, identificador: str):
        try:
            lote = self.__produto.lotes.get(identificador)

            if not lote:
                raise EntidadeNaoExistente()

            requisicao = self.limite.atualizar(lote.objeto_limite_detalhado())

            botao = requisicao.get("botao")
            valores = requisicao.get("valores")

            if botao is None:
                self.listar()
                return

            lote.data_validade = valores.get("data_validade")
            lote.quantidade = int(valores.get("quantidade"))

            self.__produto.remover_lote(identificador)
            self.__produto.add_lote(lote)

            self.listar()
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

    def deletar(self, identificador: str):
        try:
            if self.__produto.lotes.get(identificador):
                self.__produto.remover_lote(identificador)

            self.listar()
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

        for lote in self.__produto.lotes.values():
            resp.append(lote.objeto_limite())

        return resp

    @staticmethod
    def lista_para_lote(lista: dict) -> Lote:
        validacao_tipo(lista, dict)

        return Lote(
            lista["data_validade"],
            int(lista["quantidade"]),
        )
