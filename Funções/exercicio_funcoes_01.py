# Crie uma função que multiplica todos os argumentos não nomeados
# recebidos.
# Retorne o total para uma variável e mostre o valor da variável.

def multiplicar(*numeros):
    total = 1
    for numero in numeros:
        total *= numero
    return total

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é Par'
    return f'{numero} é Ímpar'


