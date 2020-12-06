from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_lote import ControleLote
from app.source.controle.controle_registro import ControleRegistro
from app.source.controle.controle_categoria import ControleCategoria
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.entidade.produto_consumivel import ProdutoConsumivel
from app.source.entidade.produto_perecivel import ProdutoPerecivel
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException
from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_produto import LimiteProduto
from app.source.persistencia.DAO_produto import DAOproduto
from app.source.persistencia.DAO_categoria import DAOcategoria


class ControleProduto(ControleAbstrato):
    def __init__(self):
        super().__init__()
        self.entity_manager = DAOproduto()

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
            opcao = self.limite.listar(self.exportar_entidades())

            ControleRegistro.adiciona_registro(
                "Moveu da Listagem de Produtos.",
                f"Requisição enviada pelo usuário:\n{opcao}"
            )

            if opcao is None:
                return

            botao = opcao.get('botao')
            valores = opcao.get("valores")
            identificador = ""

            if valores and isinstance(valores, dict):
                identificador = valores.get("tabela")
                if identificador and isinstance(identificador, list):
                    identificador = self.entity_manager.get_all()[identificador[0]].identificador

            if botao == 'tabela':
                botao = self.limite.tabela_opcoes()

                if botao is None:
                    self.listar()
                    return

                botao = botao.get('botao')

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
        try:
            nome_funcao = "criar"

            rotas = self.rotas(nome_funcao)
            requisicao = self.limite.criar()

            botao = requisicao.get('botao')

            if botao is None:
                self.selecione_rota(rotas, botao, self.listar)

            produto = self.lista_para_produto(requisicao.get("valores"))

            if requisicao.get("tem_categorias"):
                produto.categorias = self.categorias()

            if isinstance(produto, ProdutoPerecivel):
                produto.lotes = ControleLote().listar()

            self.adicionar_entidade(produto)
            ControleRegistro.adiciona_registro("Criou produto.", f"Requisição enviada pelo usuário:\n{requisicao}")
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
            nome_funcao = "atualizar"

            rotas = self.rotas(nome_funcao)
            self.limite.atualizar()
            escolhas = self.limite.selecionar_opcao("formulario")
            produto = self.lista_para_produto(escolhas)

            if escolhas.get("tem_categorias"):
                produto.categorias = self.categorias()

            if isinstance(produto, ProdutoPerecivel):
                produto.lotes = ControleLote().listar()

            registro_produto = self.entidades[self.PRODUTO_ENTIDADE]\
                .get(escolhas.get("codigo_referencia"))

            if registro_produto is not None:
                registro_produto = registro_produto.objeto_limite_detalhado()

            self.atualizar_entidade(escolhas.get("codigo_referencia"), produto)

            ControleRegistro.adiciona_registro(
                "Atualizou produto.",
                f"Requisição enviada pelo usuário:\n{escolhas}\n\nProduto Antes da alteração:\n{registro_produto}"
            )

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

    def mostrar(self, identificador: str):
        try:
            nome_funcao = "mostrar"
            rotas = self.rotas(nome_funcao)
            escolha = self.limite.selecionar_opcao(nome_funcao)["codigo_referencia"]
            produto = self.entity_manager.get(escolha)

            if produto is not None:
                produto = produto.objeto_limite_detalhado()

            self.limite.mostrar(produto)

            ControleRegistro.adiciona_registro(
                "Visualizou detalhes de um produto.",
                f"Requisição enviada pelo usuário:\n{escolha}\n\nProduto visto:\n{produto}"
            )

            self.selecione_rota(rotas, "v", self.listar)
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

    def deletar(self, identificador: str):
        try:
            produto = self.entity_manager.get(identificador)
            self.entity_manager.remove(identificador)

            ControleRegistro.adiciona_registro(
                "Deletou produto.",
                f"Requisição enviada pelo usuário:\n{identificador}\n\nProduto Deletado:\n{produto}"
            )

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

    def categorias(self, categorias: DAOcategoria or None = None):
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
    def lista_para_produto(lista: dict) -> ProdutoAbstrato:
        validacao_tipo(lista, dict)

        if lista.get("eh_perecivel"):
            return ProdutoPerecivel(
                lista.get("codigo"),
                lista.get("nome"),
                lista.get("descricao"),
                lista.get("data_fabricacao"),
                None,
                float(lista.get("valor")),
                int(lista.get("prioridade")),
                int(lista.get("estoque")),
                int(lista.get("estoque_minimo")),
            )

        return ProdutoConsumivel(
            lista.get("codigo"),
            lista.get("nome"),
            lista.get("descricao"),
            lista.get("data_fabricacao"),
            None,
            float(lista.get("valor")),
            int(lista.get("prioridade")),
            int(lista.get("estoque")),
            int(lista.get("estoque_minimo")),
        )
