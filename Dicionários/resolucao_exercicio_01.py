perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    }
]

qnt_acertos = 0

for pergunta in perguntas:
    print(f'\nPergunta: {pergunta['Pergunta']}')
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i + 1}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')
    escolha_int = None
    acertou = False
    qnt_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if 1 <= escolha_int <= qnt_opcoes:
            if opcoes[escolha_int - 1] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qnt_acertos += 1
        print(f'\nAcertou!')
    else:
        print(f'\nBurre!')

if qnt_acertos > 0:
    print(f'Você acertou {qnt_acertos} perguntas de um total de {len(perguntas)} perguntas!')
else:
    print('Errou tudo, misericórida!')

