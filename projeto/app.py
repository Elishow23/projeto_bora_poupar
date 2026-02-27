from models import Categoria, Despesa
from bd import bd

opcao = ''

bd = bd()

while True:

    print('--- SISTEMA ME_POUPE ---')
    print('1 - Minhas despesas')
    print('2 - Relatório')
    print('0 - Sair')
    print('-------------------------')
    try:
        opcao = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Digite apenas números! Digite novamente.')
        continue

    if opcao == 0:
        print('Saindo do programa...')
        break
    elif opcao == 1:

        opcao_despesa = ''

        while True:

            print('---- DESPESAS ---')
            print('1 - Criar despesa')
            print('2 - Editar despesa')
            print('3 - Listar despesa')
            print('4 - Excluir despesa')
            print('5 - Aba categoria')
            print('0 - Menu')
            print('-----------------')

            try:
                opcao_despesa = int(input('Digite a opção desejada: '))
            except ValueError:
                print('Digite apenas números! Digite novamente.')
                continue
            
            if opcao_despesa == 0:
                print('Saindo das despesas...')
                break
            elif opcao_despesa == 1:
                print('Criar despesa')

                categorias = bd.listar_categoria()
                
                if categorias is None:
                    print('Cadastre uma categoria para suas despesas!')
                    continue
                else:
                    try:
                        descricao = input('Digite a descrição da despesa: ')
                        valor = float(input('Digite o valor da despesa: R$ '))
                    except ValueError:
                        print('Atenção, para "Descrição" insira texto. Para valor, número em r$: . ')
                        continue
                    try:
                        data = input('Digite a data da despesa "dd/mm/aaaa": ')
                    except ValueError:
                        print('Digite no formato "dd/mm/aaaa".')
                        continue

                    for categoria in categorias:
                        print(f'ID: {categoria[0]} | Tipo: {categoria[1]} | Limite: R$ {categoria[2]:.2f}')
                    
                    try:
                        categoria = int(input('Selecione o tipo da sua dispesa de acordo com o que você já tem cadastrado: '))
                    except ValueError:  
                        print('Digite apenas números! Digite novamente.')
                        continue

                    d1 = Despesa(0, descricao, valor, data, categoria)

                    bd.inserir_despesa(d1)
            
            elif opcao_despesa == 2:
                print('Editar despesa')
                despesa = bd.listar_despesas()

                if not despesa:
                    print('Nenhuma despesa cadastrada.')
                else:
                    for d in despesa:
                        print(f"ID: {d[0]} | {d[1]} | R$ {d[2]} | {d[3]} | Categoria: {d[4]}")
                    try:
                        busca_id = int(input('Digite o id da despesa que deseja editar: '))
                    except ValueError:
                        print('Digite apenas números! Digite novamente.')
                        continue
                    try:
                        descricao = input('Digite a descrição da despesa: ')
                    except ValueError:
                        print('Digite apenas texto! Digite novamente.')
                        continue
                    try:
                        valor = float(input('Digite o valor da despesa: R$'))
                    except ValueError:
                        print('Digite apenas números em R$! Digite novamente.')
                        continue
                    try:
                        data = input('Digite a data da despesa (dd/mm/aaaa): ')
                    except ValueError:
                        print('Digite no formato (dd/mm/aaaa)! Tente novamente.')
                        continue

                    try:
                        categoria = int(input('Selecione o tipo da sua dispesa de acordo com o que você já tem cadastrado: '))
                    except ValueError:
                        print('Digite apenas números! Digite novamente.')
                        continue

                    d1 = Despesa(0, descricao, valor, data, categoria)
                    bd.atualizar_despesa(d1, busca_id)
            
            elif opcao_despesa == 3:
                print('Listar despesas')
                despesas = bd.listar_despesas()

                if not despesas:
                    print('Nenhuma despesa cadastrada.')
                else:
                    for d in despesas:
                        print(f"ID: {d[0]} | {d[1]} | R$ {d[2]} | {d[3]} | Categoria: {d[4]}")

            elif opcao_despesa == 4:
                print('Excluir despesa')

                despesas = bd.listar_despesas()

                if not despesas:
                    print('Nenhuma despesa cadastrada.')
                else:
                    for d in despesas:
                        print(f"ID: {d[0]} | {d[1]} | R$ {d[2]} | {d[3]} | Categoria: {d[4]}")
                
                    try:
                        busca_id = int(input('Digite o id da despesa que deseja excluir: '))
                    except ValueError:
                        print('Digite apenas números! Digite novamente.')
                        continue
                    bd.excluir_despesa(busca_id)
            
            elif opcao_despesa == 5:
                print('Categoria')
                opcao_categoria = ''

                while True:
                    print('--- CATEGORIA ---')
                    print('1 - Adicionar categoria')
                    print('2 - Listar categoria')
                    print('3 - Editar limite mensal')
                    print('0 - Menu')
                    print('-----------------')

                    try:
                        opcao_categoria = int(input('Digite a opção desejada: '))
                    except ValueError:
                        print('Digite apenas números! Digite novamente.')
                        continue

                    if opcao_categoria == 0:
                        print('Saindo das categorias...')
                        break
                    elif opcao_categoria == 1:
                        print('Criar categoria')
                        try:
                            print('Categoria de despesas: Fixa, Variavel, Essencial, Diarias.')
                            print('+-------------+-------------------------+-----------------+')
                            print('|ID categoria | Tipo de despesa         | Exemplo         |')
                            print('+-------------+-------------------------+-----------------+')
                            print('| 1. Fixa     | Despesas recorrentes    | Aluguel, contas |')
                            print('| 2. Variavel | Despesas que podem mudar| Lazer, compras  |')
                            print('| 3. Essencial| Despesas necessárias    | Alimentação,Saúd|')
                            print('| 4. Diarias  | para o dia a dia        | transporte      |')
                            print('+-------------+-------------------------+-----------------|')
                            tipo = int(input('Digite o tipo da categoria, ex: 1 para Fixa, 2 para Variavel: '))
                            if not tipo in [1, 2, 3, 4]:
                                print('Opção inválida! Digite novamente.')
                                continue
                        except ValueError:
                            print('Digite apenas números! Digite novamente.')
                            continue
                        try:
                            limite_mensal = float(input('Digite o limite mensal da categoria: R$ '))
                        except ValueError:
                            print('Digite apenas números em R$! Digite novamente. ')
                            continue

                        c1 = Categoria(0, tipo, limite_mensal)
                        bd.inserir_categoria(c1)

                    elif opcao_categoria == 2:
                        print('Listar categorias')
                        categoria = bd.listar_categoria()

                        if not categoria:
                            print('Nenhuma categoria cadastrada.')
                        else:
                            for c in categoria:
                                print(f"ID: {c[0]} | Tipo: {c[1]} | Limite: R$ {c[2]:.2f}")

                    elif opcao_categoria == 3:
                        print('Editar limite mesal da categoria')

                        categorias = bd.listar_categoria()

                        if not categorias:
                            print("Nenhuma categoria cadastrada.")
                        else:
                            for categoria in categorias:
                                print (f'ID: {categoria[0]} | Tipo: {categoria[1]} | Limite: R$ {categoria[2]:.2f}')

                            try:                            
                                id_busca = int(input('Digite o id da categoria que deseja editar: '))
                                novo_limite = float(input('Digite o novo limite mensal da categoria: R$ '))
                                bd.atualizar_categoria(novo_limite, id_busca)
                            except ValueError:
                                print('Digite apenas números.')
                                continue
                        
                            

    
    elif opcao == 2:
        print('Relatório')
        
        opcao_relatorio = ''

        while True:
            print('--- RELATÓRIO ---')
            print('1 - Total de despesas')
            print('2 - Despesas por categoria')
            print('0 - Menu')
            print('-----------------')

            try:
                opcao_relatorio = int(input('Digite a opção desejada: '))
            except ValueError:
                print('Digite apenas números! Digite novamente.')
                continue

            if opcao_relatorio == 0:
                print('Saindo do relatório...')
                break
            elif opcao_relatorio == 1:
                print('Total de despesas')
                bd.valor_total_despesas()
            elif opcao_relatorio == 2:
                print('Despesas por categoria')
                bd.total_despesas_por_categoria()

    else:
        print('Opção inválida! Digite novamente.')


    

    