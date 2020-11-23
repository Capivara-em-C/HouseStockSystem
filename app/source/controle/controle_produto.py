from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_lote import ControleLote
from app.source.controle.controle_registro import ControleRegistro
from app.source.entidade.produto_abstrato import ProdutoAbstrato
from app.source.entidade.produto_consumivel import ProdutoConsumivel
from app.source.entidade.produto_perecivel import ProdutoPerecivel
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException
from app.source.helpers.setter import validacao_tipo
from app.source.limite.limite_lote import LimiteLote
from app.source.limite.limite_produto import LimiteProduto


class ControleProduto(ControleAbstrato):
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
            self.limite.listar(self.exportar_entidades())

            opcao = self.limite.selecionar_opcao(nome_funcao)["menu"]

            ControleRegistro.adiciona_registro(
                "Moveu da Listagem de Produtos.",
                f"Requisição enviada pelo usuário:\n{opcao}"
            )

            retorno = self.selecione_rota(rotas, opcao, self.listar)

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
            self.limite.criar()
            escolhas = self.limite.selecionar_opcao("formulario")
            produto = self.lista_para_produto(escolhas)

            if escolhas.get("tem_categorias"):
                produto.categorias = self.categorias()

            if isinstance(produto, ProdutoPerecivel):
                produto.lotes = ControleLote(LimiteLote()).listar()

            self.adicionar_entidade(self.PRODUTO_ENTIDADE, produto)

            ControleRegistro.adiciona_registro("Criou produto.", f"Requisição enviada pelo usuário:\n{escolhas}")

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

    def atualizar(self):
        try:
            nome_funcao = "atualizar"

            rotas = self.rotas(nome_funcao)
            self.limite.atualizar()
            escolhas = self.limite.selecionar_opcao("formulario")
            produto = self.lista_para_produto(escolhas)

            if escolhas.get("tem_categorias"):
                produto.categorias = self.categorias()

            if isinstance(produto, ProdutoPerecivel):
                produto.lotes = ControleLote(LimiteLote()).listar()

            registro_produto = self.entidades[self.PRODUTO_ENTIDADE]\
                .get(escolhas.get("codigo_referencia"))

            if registro_produto is not None:
                registro_produto = registro_produto.objeto_limite_detalhado()

            self.atualizar_entidade(self.PRODUTO_ENTIDADE, produto)

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

    def mostrar(self):
        try:
            nome_funcao = "mostrar"
            rotas = self.rotas(nome_funcao)
            escolha = self.limite.selecionar_opcao(nome_funcao)["codigo_referencia"]
            produto = self.entidades[self.PRODUTO_ENTIDADE].get(escolha)

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

    def deletar(self):
        try:
            nome_funcao = "deletar"
            rotas = self.rotas(nome_funcao)
            escolha = self.limite.selecionar_opcao(nome_funcao)["codigo_referencia"]
            registro_produto = self.entidades[self.PRODUTO_ENTIDADE].get(escolha)

            if registro_produto is not None:
                registro_produto = registro_produto.objeto_limite_detalhado()

            self.remover_entidade(self.PRODUTO_ENTIDADE, self.entidades[self.PRODUTO_ENTIDADE].get(escolha))
            ControleRegistro.adiciona_registro(
                "Deletou produto.",
                f"Requisição enviada pelo usuário:\n{escolha}\n\nProduto Deletado:\n{registro_produto}"
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

    def categorias(self, categorias: dict or None = None):
        if categorias is None:
            categorias = {}

        self.limite.categorias()
        escolha = self.limite.selecionar_opcao("categorias")["codigo_referencia"]
        categoria = self.entidades[self.CATEGORIA_ENTIDADE].get(escolha)

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
                lista["codigo_referencia"],
                lista["nome"],
                lista["descricao"],
                lista["data_fabricacao"],
                None,
                float(lista["valor"]),
                int(lista["prioridade"]),
                int(lista["estoque"]),
                int(lista["estoque_minimo"]),
            )

        return ProdutoConsumivel(
            lista["codigo_referencia"],
            lista["nome"],
            lista["descricao"],
            lista["data_fabricacao"],
            None,
            float(lista["valor"]),
            int(lista["prioridade"]),
            int(lista["estoque"]),
            int(lista["estoque_minimo"]),
        )
