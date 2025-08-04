import matplotlib.pyplot as plt


def faturamento_mensal_(df):
    faturamento_mensal = df.groupby("mes")["faturamento_total"].sum()

    # 📊 - Visualização
    faturamento_mensal.plot(kind="bar", figsize=(10, 5), title="Faturamento Mensal")
    plt.ylabel("Faturamento (R$)")
    plt.xlabel("Mês")
    plt.tight_layout()
    plt.show()

    print('\nFATURAMENTO MENSAL')
    print(faturamento_mensal)


def faturamento_loja_(df):
    faturamento_loja = df.groupby("nome_loja")["faturamento_total"].sum().sort_values(ascending= False)

    faturamento_loja.plot(kind="barh", title="Faturamento por loja")
    plt.xlabel("Faturamento (R$)")
    plt.ylabel("Loja")
    plt.tight_layout()
    plt.show()

    print('\nFATURAMENTO POR LOJA')
    print(faturamento_loja)


def produtos_mais_vendidos(df):
    produto_mais_vendido = df.groupby("nome_produto")["quantidade"].sum()
    print('\nPRODUTO MAIS VENDIDO')
    print(f'Produto: {produto_mais_vendido.idxmax()} - Quantidade: {produto_mais_vendido.max()}')


def faturamento_categoria_(df):
    maior_faturamento = df.groupby("categoria")["faturamento_total"].sum()

    # 📊 - Visualização
    maior_faturamento.sort_values().plot(kind="barh", title="Faturamento por Categoria")
    plt.xlabel("Faturamento (R$)")
    plt.ylabel("Categoria")
    plt.tight_layout()
    plt.show()


def faturamento_estado_(df):
    faturamento_estado = df.groupby("estado")["faturamento_total"].sum()
    
    print('\nFATURAMENTO POR ESTADO\n', faturamento_estado)
    faturamento_estado.plot(kind='pie', title='Faturamento por Estado', autopct='%1.1f%%')
    plt.tight_layout()
    plt.show()


def faturamento_diario_(df):
    vendas_por_dia = df.groupby("dia_semana")["faturamento_total"].sum()

    print(vendas_por_dia)

    vendas_por_dia.plot(kind="bar", title="MELHOR DIA PARA VENDAS")
    plt.xlabel('Dias')
    plt.ylabel('Reais (R$)')
    plt.tight_layout()
    plt.show()