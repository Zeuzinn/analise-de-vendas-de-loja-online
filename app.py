from views.lojas import lojas
from views.vendas import vendas
from views.produtos import produtos
import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.float_format = 'R${:,.2f}'.format

vendas = vendas.merge(produtos, on="id_produto")
vendas = vendas.merge(lojas, on="id_loja")

df = vendas

print(df.head(1))

df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.to_period('M')

df["faturamento_total"] = df["quantidade"] * df["preco_unitario"]


# Faturamento total por mês
faturamento_mensal = df.groupby("mes")["faturamento_total"].sum()

# 📊 - Visualização
faturamento_mensal.plot(kind="bar", figsize=(10, 5), title="Faturamento Mensal")
plt.ylabel("Faturamento (R$)")
plt.xlabel("Mês")
plt.tight_layout()
plt.show()

print('\nFATURAMENTO MENSAL')
print(faturamento_mensal)


# Faturamento por loja
faturamento_loja = df.groupby("nome_loja")["faturamento_total"].sum().sort_values(ascending= False)

faturamento_loja.plot(kind="barh", title="Faturamento por loja")
plt.xlabel("Faturamento (R$)")
plt.ylabel("Loja")
plt.tight_layout()
plt.show()

print('\nFATURAMENTO POR LOJA')
print(faturamento_loja)


# Produtos mais vendidos (quantidade)
produto_mais_vendido = df.groupby("nome_produto")["quantidade"].sum()

print('\nPRODUTO MAIS VENDIDO')
print(f'Produto: {produto_mais_vendido.idxmax()} - Quantidade: {produto_mais_vendido.max()}')


# Categoria com maior faturamento
maior_faturamento = df.groupby("categoria")["faturamento_total"].sum()

# 📊 - Visualização
maior_faturamento.sort_values().plot(kind="barh", title="Faturamento por Categoria")
plt.xlabel("Faturamento (R$)")
plt.ylabel("Categoria")
plt.tight_layout()
plt.show()

print('\nCATEGORIA COM MAIOR FATURAMENTO')
print(f'{maior_faturamento.idxmax()} - R${maior_faturamento.max():,.2f}')


# Ticket médio por venda
media_por_venda = df.groupby("id_venda")["faturamento_total"].sum()

print('\nMÉDIA POR VENDA')
print(f'R${media_por_venda.mean():,.2f}')


# Faturamento por estado
faturamento_estado = df.groupby("estado")["faturamento_total"].sum()

print('\nFATURAMENTO POR ESTADO\n', faturamento_estado)


# Maior venda por loja
mais_vendido_por_loja = df.groupby(["nome_loja", "nome_produto"])["quantidade"].sum().sort_values(ascending=False)

print('\nMAIS VENDIDO POR LOJA\n',mais_vendido_por_loja.head(5))


# Melhor dia da semana para vendas
df["dia_semana"] = df["data"].dt.day_name()
vendas_por_dia = df.groupby("dia_semana")["faturamento_total"].sum()

print(vendas_por_dia)

vendas_por_dia.plot(kind="bar", title="MELHOR DIA PARA VENDAS")
plt.xlabel('Dias')
plt.ylabel('Reais (R$)')
plt.tight_layout()
plt.show()