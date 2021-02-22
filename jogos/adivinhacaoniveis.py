import random

def jogar():
    print("**********************************")
    print("bem vindos ao jogo de adivinhação!")
    print("**********************************")


    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) easy (2) medium (3) hard")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativas {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um valor entre 1 e 100: "))
        print("VocÊ digitou ", chute)
    #valores c/ ponto flutuante pode ser usado "R$ {:.2f}".format(1.59)
        if(chute < 1 or chute > 100): #or || and
            print("Warning: É necessário digitar valores entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")
if(__name__ == "__main__"):
    jogar()
