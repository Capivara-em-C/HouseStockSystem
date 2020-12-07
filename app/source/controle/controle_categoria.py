from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_registro import ControleRegistro
from app.source.entidade.categoria import Categoria
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException
from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_categoria import LimiteCategoria
from app.source.persistencia.DAO_categoria import DAOCategoria
from app.source.persistencia.DAO_produto import DAOProduto


class ControleCategoria(ControleAbstrato):
    def __init__(self):
        super().__init__()
        self.entity_manager = DAOCategoria()

    @staticmethod
    def classe_limite() -> type:
        return LimiteCategoria

    def listar(self) -> None:
        try:
            nome_funcao = "listar"

            rotas = self.rotas(nome_funcao)
            requisicao = self.limite.listar(self.exportar_entidades())

            ControleRegistro.adiciona_registro(
                "Moveu da Listagem de Categorias.",
                f"Requisição enviada pelo usuário:\n{requisicao}"
            )

            if requisicao.get("botao") is None:
                return None

            botao = requisicao.get('botao')
            valores = requisicao.get("valores")
            identificador = ""

            if valores and isinstance(valores, dict) and botao == 'tabela':
                identificador = valores.get("tabela")
                if identificador and isinstance(identificador, list) and len(identificador) > 0:
                    if len(self.entity_manager.get_all()) < 1:
                        self.listar()
                        return
                    identificador = self.entity_manager.get_all()[identificador[0]].identificador
                else:
                    self.listar()
                    return

            if botao == 'tabela':
                botao = self.limite.tabela_opcoes().get('botao')

                if botao is None:
                    self.listar()
                    return

            if botao in ("editar", "mostrar", "apagar"):
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
        requisicao = None

        try:
            requisicao = self.limite.criar()

            if requisicao.get("botao") is None:
                self.listar()
                return

            produto = self.lista_para_categoria(requisicao.get("valores"))

            self.adicionar_entidade(produto)

            self.listar()
        except ValueError as err:
            self.limite.erro(
                "Algum argumento passado foi do tipo errado[Número ou palavra]\n" +
                "(Exemplo: No cadastro de um produto você passou uma letra para o valor)."
            )
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except (
                TipoNaoCompativelException,
                CodigoReferenciaDuplicadoException,
        ) as err:
            self.limite.erro(err)
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
            self.listar()
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
        ) as err:
            self.limite.erro(err)
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except Exception as err:
            self.limite.erro("Erro inesperado ocorreu!")
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        finally:
            ControleRegistro.adiciona_registro("Criou produto.", f"Requisição enviada pelo usuário:\n{requisicao}")

    def atualizar(self, identificador: str):
        registro_produto = None
        requisicao = None

        try:
            registro_categoria = self.entity_manager.get(identificador)

            requisicao = self.limite.atualizar(
                registro_categoria.objeto_limite_detalhado()
            )

            if requisicao.get("botao") is None:
                self.listar()
                return

            categoria = self.lista_para_categoria(
                requisicao.get("valores"),
                registro_categoria
            )

            self.atualizar_entidade(categoria, identificador)

            self.listar()
        except ValueError as err:
            self.limite.erro(
                "Algum argumento passado foi do tipo errado[Número ou palavra]\n" +
                "(Exemplo: No cadastro de um produto você passou uma letra para o valor)."
            )
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except (
                TipoNaoCompativelException,
                CodigoReferenciaDuplicadoException,
        ) as err:
            self.limite.erro(err)
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
        ) as err:
            self.limite.erro(err)
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except Exception as err:
            self.limite.erro("Erro inesperado ocorreu!")
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        finally:
            ControleRegistro.adiciona_registro(
                "Atualizou categoria.",
                f"Requisição enviada pelo usuário:\n{requisicao}\n" +
                "\nCategoria Antes da alteração:\n{registro_categoria}"
            )

    def deletar(self, identificador: str):
        try:
            categoria = self.entity_manager.get(identificador)
            self.entity_manager.remove(identificador, False)

            produtos = DAOProduto().get_all()
            for produto in produtos:
                if produto.categorias.get(identificador):
                    del(produto.categorias[identificador])
                    DAOProduto().remove(produto.identificador)
                    DAOProduto().add(produto.identificador, produto)

            ControleRegistro.adiciona_registro(
                "Deletou categoria.",
                f"Requisição enviada pelo usuário:\n{categoria.objeto_limite_detalhado()}\n" +
                "\nCategoria deletada:\n{registro_categoria}"
            )

            self.listar()
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
                TipoNaoCompativelException,
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

    def voltar_listagem(self) -> None:
        return None

    @staticmethod
    def lista_para_categoria(lista: dict, categoria: Categoria or None = None) -> Categoria:
        validacao_tipo(lista, dict)

        if categoria is None:
            categoria = Categoria(lista.get("identificador"))

        categoria.identificador = lista.get("identificador") if lista.get("identificador") else categoria.identificador
        categoria.nome = lista.get("nome") if lista.get("nome") else categoria.nome

        return categoria

    @staticmethod
    def classe_entidade() -> type:
        return Categoria

    def atualizar_entidade(self, entidade: Categoria, identificador: str or None = None):
        super().atualizar_entidade(entidade=entidade, identificador=identificador)

        produtos = DAOProduto().get_all()
        for produto in produtos:
            if produto.categorias.get(identificador):
                produto.categorias[identificador] = entidade
                DAOProduto().remove(produto.identificador)
                DAOProduto().add(produto.identificador, produto)
