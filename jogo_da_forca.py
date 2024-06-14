import random

def escolher_palavra(palavras):
    return random.choice(palavras)

def exibir_forca(tentativas):
    forca = """
        _______
        |     |
        |     O
        |    /|\\
        |     |
        |    / \\
        -
    """
    if tentativas <= 6:
        return forca[:31 - tentativas]
    else:
        return forca

def jogar():
    palavras = ['desenvolvimento', 'tecnologia', 'lógica', 'programação', 'tendências']
    palavra_secreta = escolher_palavra(palavras)
    palavra_oculta = ['_' for _ in palavra_secreta]
    letras_tentadas = []
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_forca(tentativas))

    while True:
        letra = input("Digite uma letra: ")
        if letra in letras_tentadas:
            print("Você já tentou essa letra!")
            continue
        letras_tentadas.append(letra)
        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
        print(" ".join(palavra_oculta))
        print(exibir_forca(tentativas))
        if "_" not in palavra_oculta:
            print("Parabéns! Você ganhou!")
            break
        elif tentativas == 6:
            print("Você perdeu! A palavra era", palavra_secreta)
            break

    print("Obrigado por jogar! Volte sempre!")

jogar()