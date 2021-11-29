import random


def jogar():
    # Executa o jogo forca
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0)

    # Variaveis internas do jogo
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0

    # Variaveis de configuração do jogo
    max_erros = 7

    # Jogo
    print(letras_acertadas)
    while not enforcou and not acertou:
        # Loop principal de execução do jogo
        print("Você tem {} de {} vidas".format(erros, max_erros))
        chute = pede_chute()

        if chute in palavra_secreta:
            # Acertou chute
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            # Errou chute
            erros += 1
            desenha_forca(erros)

        enforcou = erros == max_erros
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")


def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0):
    # Seletor de palavra do jogo
    palavras = []
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(primeira_linha_valida, len(palavras))].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ").strip().upper()
    return chute


def marca_chute_correto(chute, palavra, letras_acertadas):
    # Acertou chute
    index = 0
    for letra in palavra:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


# Self-execution
if __name__ == "__main__":
    jogar()
