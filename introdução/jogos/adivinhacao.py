import random


def jogar():
    # Executa o jogo adivinhação
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Variáveis do jogo
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    # Nível de dificuldade
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    # Laço do Jogo de Advinhação
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou!")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi MAIOR que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi MENOR que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)  # 40-60=20 |60-40=20
            # pontos perdidos na rodada
            pontos = pontos - pontos_perdidos
            # pontos perdidos totais
            if rodada == total_de_tentativas:
                print("O número secreto era {}".format(numero_secreto))

    print("Você fez {} pontos!".format(pontos))
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
