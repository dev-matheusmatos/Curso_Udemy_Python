frase = 'O Python é uma linguagem de programação multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

i = 0
qnt_mais_frequente = 0
letra_mais_frequente = ''

while i < len(frase):

    letra_atual = frase[i]
    i += 1

    if letra_atual == ' ':
        continue

    qnt_letra_atual = frase.count(letra_atual)

    if qnt_letra_atual > qnt_mais_frequente:

        qnt_mais_frequente = qnt_letra_atual
        letra_mais_frequente = letra_atual

print(f'A letra mais frequente foi a letra {letra_mais_frequente}, que apareceu {qnt_mais_frequente} vezes!')
