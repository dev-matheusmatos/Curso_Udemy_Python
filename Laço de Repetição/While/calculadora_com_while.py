
while True:

    print(f'\n{"=" * 41}')
    print(f'{" " * 15}CALCULADORA{" " * 15}')
    print(f'{"=" * 41}')

    numero_01 = float(input('\nInforme o primero valor: '))
    numero_02 = float(input('Informe o segundo valor: '))
    operacao = input('Informe a operação (+, -, *, / e %): ')

    print()

    if operacao == '+':

        soma = numero_01 + numero_02
        print(f'{numero_01} + {numero_02} = {soma}')

    elif operacao == '-':

        subtracao = numero_01 - numero_02
        print(f'{numero_01} - {numero_02} = {subtracao}')

    elif operacao == '*':

        multiplicacao = numero_01 * numero_02
        print(f'{numero_01} x {numero_02} = {multiplicacao}')

    elif operacao == '/':

        divisao = numero_01 / numero_02
        print(f'{numero_01} / {numero_02} = {divisao}')

    elif operacao == '%':

        modulo = numero_01 % numero_02
        print(f'{numero_01} % {numero_02} = {modulo}')

    else:

        print('Operação inválida!')

    opcao = input('''\nDeseja sair? 
    
[1] SIM
[Enter] Continuar

''')

    if opcao == '1':
        print('\nObrigado por utilizar a calculadora!')
        break
