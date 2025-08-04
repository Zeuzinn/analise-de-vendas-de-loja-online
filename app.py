import pandas as pd
from views.lojas import lojas
from views.vendas import vendas
from views.produtos import produtos
from controllers.interation import main

pd.options.display.float_format = 'R${:,.2f}'.format

vendas = vendas.merge(produtos, on="id_produto")
vendas = vendas.merge(lojas, on="id_loja")

# Pré-processamento
vendas["data"] = pd.to_datetime(vendas["data"])
vendas["mes"] = vendas["data"].dt.to_period('M')
vendas["faturamento_total"] = vendas["quantidade"] * vendas["preco_unitario"]
vendas["dia_semana"] = vendas["data"].dt.day_name()

df = vendas

if __name__ == "__main__":
    main(df)
