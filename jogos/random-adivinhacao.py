import random

print("**********************************")
print("bem vindos ao jogo de adivinhação!")
print("**********************************")


numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

print(numero_secretoos)

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
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto")

print("Fim de jogo!")