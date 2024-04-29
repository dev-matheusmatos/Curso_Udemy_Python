cpf = input('Informe o CPF: ')

mult = 10
soma = 0
digito_01 = 0
digitp_02 = 0

for digito in range(cpf[9]):
    soma += int(digito) * mult
    mult -= 1

if soma % 11 < 2:
    digito_01 = 0
else:
    digito_01 = 11 - (soma % 2)

soma = 0
mult = 11

for digito in cpf[10]:
    soma += int(digito) * mult
    mult -= 1

if soma % 11 < 2:
    digito_02 = 0
else:
    digito_02 = 11 - (soma % 2)

if digito_01 == int(cpf[9]) and digito_02 == int(cpf[10]):
    print('CPF válido')
else:
    print('CPF inválido')