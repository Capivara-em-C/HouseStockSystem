from traceback import format_exc

from app.source.controle.controle_abstrato import ControleAbstrato
from app.source.controle.controle_registro import ControleRegistro
from app.source.entidade.categoria import Categoria
from app.source.exception.codigo_referencia_duplicado_exception import CodigoReferenciaDuplicadoException
from app.source.exception.metodo_nao_permitido_exception import MetodoNaoPermitidoException
from app.source.exception.rota_inexistente_exception import RotaInexistenteException
from app.source.exception.tipo_nao_compativel_exception import TipoNaoCompativelException
from app.source.helpers.setter import validacao_tipo
from app.source.limite_console.limite_categoria import LimiteCategoria
from app.source.persistencia.DAO_categoria import DAOCategoria


class ControleCategoria(ControleAbstrato):
    def __init__(self):
        super().__init__()
        self.entity_manager = DAOCategoria()

    @staticmethod
    def classe_limite() -> type:
        return LimiteCategoria

    def listar(self):
        try:
            nome_funcao = "listar"

            rotas = self.rotas(nome_funcao)
            self.limite.listar(self.exportar_entidades())

            opcao = self.limite.selecionar_opcao(nome_funcao)["menu"]

            ControleRegistro.adiciona_registro(
                "Moveu da Listagem de Categorias.",
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
            rotas = self.rotas("criar")
            self.limite.criar()
            escolhas = self.limite.selecionar_opcao("criar")

            self.adicionar_entidade(self.CATEGORIA_ENTIDADE, self.lista_para_categoria(escolhas))

            ControleRegistro.adiciona_registro("Criou Categoria.", f"Requisição enviada pelo usuário:\n{escolhas}")

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

    def atualizar(self, identificador: str):
        try:
            rotas = self.rotas("atualizar")
            self.limite.criar()
            escolhas = self.limite.selecionar_opcao("atualizar")

            registro_categoria = self.entidades.get(escolhas.get("codigo_referencia"))

            if registro_categoria is not None:
                registro_categoria = registro_categoria.objeto_limite()

            self.atualizar_entidade(registro_categoria.identificador, self.lista_para_categoria(escolhas))

            ControleRegistro.adiciona_registro(
                "Atualizou categoria.",
                f"Requisição enviada pelo usuário:\n{escolhas}\n\nCategoria Antes da alteração:\n{registro_categoria}"
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

    def deletar(self):
        try:
            rotas = self.rotas("deletar")
            self.limite.criar()
            escolha = self.limite.selecionar_opcao("deletar")["codigo_referencia"]
            registro_categoria = self.entidades.get(escolha)

            if registro_categoria is not None:
                registro_categoria = registro_categoria.objeto_limite()

            for entidade in self.entidades["produtos"].values():
                if entidade.categorias.get(escolha) is not None:
                    del(entidade.categorias[escolha])

            self.remover_entidade(escolha)

            ControleRegistro.adiciona_registro(
                "Deletou categoria.",
                f"Requisição enviada pelo usuário:\n{escolha}\n\nCategoria deletada:\n{registro_categoria}"
            )

            self.selecione_rota(rotas, "v", self.listar)
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
    def lista_para_categoria(lista: dict) -> Categoria:
        validacao_tipo(lista, dict)

        return Categoria(
            lista["codigo_referencia"],
            lista["nome"],
        )

    @staticmethod
    def classe_entidade() -> type:
        return Categoria
