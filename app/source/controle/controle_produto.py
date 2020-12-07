from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_lote import ControleLote
from app.source.controle.controle_registro import ControleRegistro
from app.source.controle.controle_categoria import ControleCategoria
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.entidade.produto_perecivel import ProdutoPerecivel
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.entidade_nao_existente import EntidadeNaoExistente
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException
from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_produto import LimiteProduto
from app.source.persistencia.DAO_produto import DAOProduto
from app.source.persistencia.DAO_categoria import DAOCategoria


class ControleProduto(ControleAbstrato):
    def __init__(self):
        super().__init__()
        self.entity_manager = DAOProduto()

    @staticmethod
    def classe_limite() -> type:
        return LimiteProduto

    @staticmethod
    def classe_entidade() -> type:
        return ProdutoAbstrato

    def listar(self):
        try:
            nome_funcao = "listar"

            rotas = self.rotas(nome_funcao)
            requisicao = self.limite.listar(self.exportar_entidades())

            ControleRegistro.adiciona_registro(
                "Moveu da Listagem de Produtos.",
                f"Requisição enviada pelo usuário:\n{requisicao}"
            )

            botao = requisicao.get('botao')

            if botao is None:
                return

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
                EntidadeNaoExistente,
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

            produto = self.lista_para_produto(requisicao.get("valores"))

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
            registro_produto = self.entity_manager.get(identificador)

            requisicao = self.limite.atualizar(registro_produto.objeto_limite_detalhado())
            botao = requisicao.get("botao")

            if botao is None:
                self.listar()
                return

            produto = self.lista_para_produto(
                requisicao.get("valores"),
                registro_produto
            )

            self.atualizar_entidade(produto, identificador)

            if botao == "categorias":
                produto.categorias = self.categorias()

            if botao == "lotes":
                ControleLote(produto=produto).listar()

            self.atualizar_entidade(produto, identificador)

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
                EntidadeNaoExistente,
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
            if registro_produto:
                registro_produto = registro_produto.objeto_limite_detalhado()

            ControleRegistro.adiciona_registro(
                "Atualizou produto.",
                f"Requisição enviada pelo usuário:\n{requisicao}\n\nProduto Antes da alteração:\n{registro_produto}"
            )

    def mostrar(self, identificador: str):
        try:
            produto = self.entity_manager.get(identificador).objeto_limite_detalhado()

            self.limite.mostrar(produto)

            ControleRegistro.adiciona_registro(
                "Visualizou detalhes de um produto.",
                f"Requisição enviada pelo usuário:\n{identificador}\n\nProduto visto:\n{produto}"
            )

            self.listar()
        except ValueError as err:
            self.limite.erro(
                "Algum argumento passado foi do tipo errado[Número ou palavra]\n" +
                "(Exemplo: No cadastro de um produto você passou uma letra para o valor)."
            )
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())

            self.listar()
        except (
                RotaInexistenteException,
                MetodoNaoPermitidoException,
                EntidadeNaoExistente,
        ) as err:
            self.limite.erro(err)
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except Exception as err:
            self.limite.erro("Erro inesperado ocorreu!")
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())

    def deletar(self, identificador: str):
        try:
            produto = self.entity_manager.get(identificador)
            self.entity_manager.remove(identificador)

            ControleRegistro.adiciona_registro(
                "Deletou produto.",
                f"Requisição enviada pelo usuário:\n{identificador}\n\nProduto Deletado:\n{produto.objeto_limite_detalhado()}"
            )

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
                EntidadeNaoExistente,
        ) as err:
            self.limite.erro(err)
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())
        except Exception as err:
            self.limite.erro("Erro inesperado ocorreu!")
            ControleRegistro.adiciona_registro(f"Erro {err}", format_exc())

    def categorias(self, categorias: DAOCategoria or None = None):
        if categorias is None:
            categorias = {}

        self.limite.categorias()
        escolha = self.limite.selecionar_opcao("categorias")["codigo_referencia"]
        categoria = ControleCategoria.entity_manager.get(escolha)

        if categoria is not None:
            categorias[categoria.identificador] = categoria
            categorias = self.categorias(categorias)

        return categorias

    def voltar_listagem(self) -> None:
        return None

    @staticmethod
    def lista_para_produto(lista: dict, produto: ProdutoAbstrato or None = None) -> ProdutoAbstrato:
        validacao_tipo(lista, dict)

        if produto is None:
            produto = ProdutoPerecivel(lista.get("identificador"))

        validacao_tipo(propriedade=produto, tipo=ProdutoAbstrato)

        identificador = lista.get("identificador")
        nome = lista.get("nome")
        descricao = lista.get("descricao")
        data_fabricacao = lista.get("data_fabricacao")
        valor = lista.get("valor")
        prioridade = lista.get("prioridade")
        estoque_quantidade = lista.get("estoque_quantidade")
        estoque_minimo = lista.get("estoque_minimo")

        produto.identificador = identificador if identificador is not None else produto.identificador
        produto.nome = nome if nome is not None else produto.nome
        produto.descricao = descricao if descricao is not None else produto.descricao
        produto.data_fabricacao = data_fabricacao if data_fabricacao is not None else produto.data_fabricacao
        produto.valor = float(valor if valor is not None else produto.valor)
        produto.prioridade = int(prioridade if prioridade is not None else produto.prioridade)
        produto.estoque_quantidade = int(estoque_quantidade if estoque_quantidade is not None else produto.estoque_quantidade)
        produto.estoque_minimo = int(estoque_minimo if estoque_minimo is not None else produto.estoque_minimo)

        return produto
