from models import categoria, despesa
from bd import bd

opcao = ''

bd = bd()

while True:

    print('--- SISTEMA ME_POUPE ---')
    print('1 - Minhas despesas')
    print('2 - Editar categoria')
    print('0 - Sair')

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
            print('3 - Listar despesas')
            print('4 - Excluir despesa')
            print('0 - Menu')

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
                    print('Digite apenas texto! Digite novamente.')
                    continue

                bd.listar_categoria()

                try:
                    categoria = int(input('Selecione o tipo da sua dispesa de acordo com o que você já tem cadastrado: '))
                except ValueError:
                    print('Digite apenas números! Digite novamente.')
                    continue

                d1 = despesa(0, descricao, valor, data, categoria)

                bd.inserir_despesa(d1)
            
            elif opcao_despesa == 3:
                print('Listar despesas')
                bd.listar_despesa()

            elif opcao_despesa == 4:
                print('Excluir despesa')
                try:
                    busca_id = int(input('Digite o id da despesa que deseja excluir: '))
                except ValueError:
                    print('Digite apenas números! Digite novamente.')
                    continue
                bd.excluir_despesa(busca_id)

    elif opcao == 2:
        
        opcao_categoria = ''

        while True:

            print('---- CATEGORIA ----')
            print('1 - Criar categoria')
            print('2 - Editar categoria')
            print('3 - Listar categorias')
            print('4 - Excluir categoria')
            print('0 - Menu')

            try:
                opcao_categoria = int(input('Digite a opção desejada: '))
            except ValueError:
                print('Digite apenas números! Digite novamente.')
                continue

            if opcao_categoria == 0:
                print('Saindo da categoria...')
                break

            elif opcao_categoria == 1:
                print('Criar categoria')
                try:
                    tipo = input('Digite o tipo de despesas que voĉe tem, exemplo: "Fixa, Essencial, Variável"...')
                except ValueError:
                    print('Digite apenas texto! Digite novamente.')
                    continue
                try:
                    limite_mensal = float(input('Digite o limite mensal da categoria: R$'))
                except ValueError:
                    print('Digite apenas números em R$! Digite novamente.')
                    continue

                c1 = categoria(0, tipo, limite_mensal)

                bd.inserir_categoria(c1)

            elif opcao_categoria == 3:
                print('Listar categorias')
                bd.listar_categoria()


            elif opcao_categoria == 2:
                print('Editar categoria')
                bd.listar_categoria()
                try:
                    busca_id = int(input('Digite o id da categoria que deseja editar: '))
                except ValueError:
                    print('Digite apenas números! Digite novamente.')
                    continue
                try:
                    tipo = input('Digite o tipo da categoria: ')
                except ValueError:
                    print('Digite apenas texto! Digite novamente.')
                    continue
                try:
                    limite_mensal = float(input('Digite o limite mensal da categoria: R$'))
                except ValueError:
                    print('Digite apenas números em R$! Digite novamente.')
                    continue

                c1 = categoria(0, tipo, limite_mensal)
                bd.update_categoria(c1, busca_id)

            elif opcao_categoria == 4:
                print('Excluir categoria')
                try:
                    busca_id = int(input('Digite o id da categoria que deseja excluir: '))
                except ValueError:
                    print('Digite apenas números! Digite novamente.')
                    continue
                bd.excluir_categoria(busca_id)
            
            else:
                print('Opção inválida! Digite novamente.')


    else:
        print('Opção inválida! Digite novamente.')


    

    