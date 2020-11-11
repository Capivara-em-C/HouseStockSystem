from app.source.controle.controle_inicio import ControleInicio
from app.source.entidade.categoria import Categoria
from app.source.entidade.lote import Lote
from app.source.entidade.produto_consumivel import ProdutoConsumivel
from app.source.entidade.produto_perecivel import ProdutoPerecivel
from app.source.limite.limite_inicio import LimiteInicio

inicio = ControleInicio(LimiteInicio())

categorias = {
    "comida": Categoria(
        "comida",
        "Comida"
    ),
    "bebida": Categoria(
        "bebida",
        "Bebida"
    ),
    "eletricos": Categoria(
        "eletricos",
        "Elétricos"
    ),
    "banheiro": Categoria(
        "banheiro",
        "Banheiro"
    ),
    "pet": Categoria(
        "pet",
        "Pet"
    ),
    "brinquedos": Categoria(
        "brinquedos",
        "Brinquedos"
    ),
}

entidade = {
    inicio.CATEGORIA_ENTIDADE: categorias,
    inicio.PRODUTO_ENTIDADE: {
        "arroz": ProdutoPerecivel(
            identificador="arroz",
            nome="Arroz",
            descricao="Grão que absorve água rico em carboidratos, direto da fazenda do Baldo",
            data_fabricacao="14/05/2020",
            ultimo_valor=3.50,
            prioridade=5,
            estoque_quantidade=6,
            estoque_minimo=3,
            categorias={
                "comida": categorias.get("comida")
            },
            lotes={
                "30/11/2020": Lote(
                    data_validade="30/11/2020",
                    quantidade=6
                )
            }
        ),
        "feijao": ProdutoPerecivel(
            identificador="feijao",
            nome="Feijão",
            descricao="Grão cosivel, Rico em ferro (Combate a anemia)",
            data_fabricacao="23/08/2020",
            ultimo_valor=4.70,
            prioridade=5,
            estoque_quantidade=3,
            estoque_minimo=1,
            categorias={
                "comida": categorias.get("comida")
            },
            lotes={
                "30/11/2020": Lote(
                    data_validade="02/01/2021",
                    quantidade=3
                )
            }
        ),
        "copos": ProdutoConsumivel(
            identificador="copos",
            nome="Copos de vidro",
            descricao="Copos de vidro, quebram mais do que você imagina...",
            data_fabricacao="01/01/2020",
            ultimo_valor=8.70,
            prioridade=2,
            estoque_quantidade=8,
            estoque_minimo=6,
            categorias={
                "comida": categorias.get("comida")
            },
        )
    },
}
inicio.entidades = entidade
inicio.home()
