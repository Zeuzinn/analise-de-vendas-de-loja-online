from views.visuals import  (
    faturamento_categoria_,
    faturamento_estado_,
    faturamento_loja_,
    faturamento_mensal_,
    produtos_mais_vendidos,
    faturamento_diario_)


def menu():
    print('\n=== Estatísticas e Análises ===\n')
    print('[1] - Faturamento mensal')
    print('[2] - Faturamento por loja')
    print('[3] - Produtos mais vendidos')
    print('[4] - Faturamento por categoria')
    print('[5] - Faturamento por estado')
    print('[6] - Faturamento diário')
    print('[0] - Sair')

def main(df):
    while True:
        menu()
        opcao = input('ESCOLHA UMA OPÇÃO PARA VISUALIZAR: ')

        if opcao == '1':
            faturamento_mensal_(df)
        elif opcao == '2':
            faturamento_loja_(df)
        elif opcao == '3':
            produtos_mais_vendidos(df)
        elif opcao == '4':
            faturamento_categoria_(df)
        elif opcao == '5':
            faturamento_estado_(df)
        elif opcao == '6':
            faturamento_diario_(df)
        elif opcao == '0':
            print('Encerrando...')
            break
        else:
            print('Opção inválida.')