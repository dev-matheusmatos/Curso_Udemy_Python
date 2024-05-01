# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2? ',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5 * 5? ',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10 / 2? ',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    }
]

acertos = 0

for pergunta in perguntas:
    print()
    print(pergunta['Pergunta'])
    print(pergunta['Opções'])
    print()
    resposta = input()
    if resposta == pergunta['Resposta']:
        print(f'\nAcertou miseravi!')
        acertos += 1
    else:
        print(f'\nBurre!')

if acertos > 0:
    print(f'\nParabéns, você acertou {acertos} questões!')
else:
    print(f'\nNão acertou nada, misericórdia, muito burre!')
