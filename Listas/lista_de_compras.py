from lista_de_compras_imports import menu, logo

lista_compras = []

print(logo)

while True:

    print()
    print(menu)
    opcao = input()

    try:
        opcao = int(opcao)

    except ValueError:
        print('\nInforme o número da opção!')
        continue

    if opcao == 4:
        print('\nObrigado por utilizar nossa lista de compras eletrônica!')
        break

    elif opcao == 1:

        item = input('\nDigite o item: ')
        lista_compras.append(item)

    elif opcao == 2:

        indice = (input('\nInforme o número do item a ser apagado: '))

        try:
            indice = int(indice)

        except ValueError:
            print('\nNão foi digitado um número.')
            continue

        if 0 <= indice < len(lista_compras):

            del lista_compras[indice]

        else:

            print('\nO item informado não existe na lista.')

    elif opcao == 3:

        print()

        for numero, item in enumerate(lista_compras):

            print(f'{numero} \t{item}')

    else:
        print('\nInforme uma opção existente!')