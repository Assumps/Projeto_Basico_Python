import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de advinhacao!")
    print("********************************")

    numero_secreto = random.randrange(1,101) # 0.0 entre 1.0
    total_de_tentativas = 0
    pontos = 1000

    print("qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu numero entre 1 e 100: " )

        print("voce digitou " , chute_str)

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou o seu chute foi maior do que o numero secreto")
            elif(menor):
                print("voce errou o numero e menor que o numero secreto")
                pontos_perdidos = abs(numero_secreto - chute) #40 - 20 = 20 pontos perdidos
                pontos = pontos - pontos_perdidos

    print("fim de jogo")

if(__name__ == "__main__"):
    jogar()