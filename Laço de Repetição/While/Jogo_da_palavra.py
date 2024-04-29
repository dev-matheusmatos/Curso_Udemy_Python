# Faça um jogo para o usuário advinhar qual a palavra secreta.
# - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
# para o usuário digitar apenas uma letra.
# - Quando o usuário digitar uma letra, você vai conferir se a letra digitada
# está na palavra secreta.
#     - Se a letra digitada estiver na palavra secreta; exiba a letra;
#     - Se a letra digitada não estiver na palavra secreta; exiba *.
# - Faça a contagem de tentativas do seu usuário.

import random

# Lista de palavras
palavras = ["python", "programacao", "jogo", "computador", "algoritmo"]
# Escolhendo aleatoriamente uma palavra da lista
palavra_secreta = random.choice(palavras)
# Conjunto de letras corretas na palavra secreta
letras_corretas = set(palavra_secreta)
# Conjunto de letras descobertas pelo jogador
letras_descobertas = set()
# Número máximo de tentativas
max_tentativas = 7
# Número de tentativas
tentativas = 0

print("Bem-vindo ao Jogo da Forca!")
print("Adivinhe a palavra secreta.")

# Loop principal do jogo
while tentativas < max_tentativas:
    # Exibindo a palavra com as letras descobertas
    palavra_exibida = "".join(letra if letra in letras_descobertas else "*" for letra in palavra_secreta)
    print(palavra_exibida)

    # Verificando se o jogador adivinhou a palavra
    if letras_corretas == letras_descobertas:
        print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
        break

    # Solicitando uma letra ao jogador
    letra = input("Digite uma letra: ").lower()

    # Verificando se a letra já foi tentada
    if letra in letras_descobertas:
        print("Você já tentou essa letra.")
        continue

    # Verificando se a letra está correta
    if letra in letras_corretas:
        letras_descobertas.add(letra)
    else:
        tentativas += 1
        print("Letra não encontrada na palavra secreta. Tentativas restantes:", max_tentativas - tentativas)

# Verificando se o jogador excedeu o número máximo de tentativas
if tentativas == max_tentativas:
    print("Você excedeu o número máximo de tentativas. A palavra secreta era:", palavra_secreta)

