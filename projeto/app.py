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
                
                if not bd.categorias:
                    print('Cadastre uma categoria para suas despesas!')
                    continue
                else:
                    try:
                        descricao = input('Digite a descrição da despesa: ')
                    except ValueError:
                        print('Digite apenas texto! Digite novamente.')
                        continue
                    try:
                        valor = float(input('Digite o valor da despesa: R$ '))
                    except ValueError:
                        print('Digite apenas números em R$! Digite novamente. ')
                        continue
                    try:
                        data = input('Digite a data da despesa (dd/mm/aaaa): ')
                    except ValueError:
                        print('Digite apenas texto! Digite novamente.')
                        continue

                    bd.listar_categoria()
                    
                    try:
                        categoria = int(input('Selecione o tipo da sua dispesa de acordo com o que você já tem cadastrado: '))
                    except ValueError:  
                        print('Digite apenas números! Digite novamente.')
                        continue

                    d1 = Despesa(0, descricao, valor, data, categoria)

                    bd.inserir_despesa(d1)
            
            elif opcao_despesa == 2:
                print('Editar despesa')
                bd.listar_despesa()
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

                d1 = despesa(0, descricao, valor, data, categoria)
                bd.update_despesa(d1, busca_id)
            
            elif opcao_despesa == 3:
                print('Listar despesas')
                bd.listar_despesa()

            elif opcao_despesa == 4:
                print('Excluir despesa')
                if not bd.despesas:
                    print('Nenhuma despesa cadastrada para excluir.')
                    continue
                else:
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
                    print('1 - Criar categoria')
                    print('2 - Listar categoria')
                    print('3 - Excluir categoria')
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
                            print('+---------------------+---------------------------+-----------------+')
                            print('| Tipo de despesa     | Descrição                 | Exemplo         |')
                            print('+---------------------+---------------------------+-----------------+')
                            print('| Fixa                | Despesas recorrentes      | Aluguel, contas |')
                            print('| Variavel            | Despesas que podem mudar  | Lazer, compras  |')
                            print('| Essencial           | Despesas necessárias      | Alimentação,Saúd|')
                            print('| Diarias             | para o dia a dia          | transporte      |')
                            print('+--------------------+---------------------+-----------------+------|')
                            tipo = input('Digite o tipo da categoria, ex: Fixa, Variavel, Essencial, Diarias: ')
                        except ValueError:
                            print('Digite apenas texto! Digite novamente.')
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
                        bd.listar_categoria()

                    elif opcao_categoria == 3:
                        print('Excluir categoria')
                        try:
                            busca_id = int(input('Digite o id da categoria que deseja excluir: '))
                        except ValueError:
                            print('Digite apenas números! Digite novamente.')
                            continue
                        
                        bd.excluir_categoria(busca_id)
    
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
                total_despesas = sum(despesa.valor for despesa in bd.despesas)
                print(f'Total de despesas: R$ {total_despesas:.2f}')
            elif opcao_relatorio == 2:
                print('Despesas por categoria')
                categorias = {}
                for despesa in bd.despesas:
                    categoria_id = despesa.categoria
                    if categoria_id in categorias:
                        categorias[categoria_id] += despesa.valor
                    else:
                        categorias[categoria_id] = despesa.valor

                for categoria_id, total in categorias.items():
                    categoria_tipo = next((c.tipo for c in bd.categorias if c.id == categoria_id), 'Categoria desconhecida')
                    print(f'Categoria: {categoria_tipo} - Total de despesas: R$ {total:.2f}')

    else:
        print('Opção inválida! Digite novamente.')


    

    