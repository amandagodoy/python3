import forca
import adivinhacaoniveis

def escolher_jogo():
    print("**********************************")
    print("********Choice your game!*********")
    print("**********************************")


    print("(1) hangman (2) divination")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("jogando hangman")
        forca.jogar()
    elif(jogo == 2):
        print("jogando divination")
        adivinhacaoniveis.jogar()

if(__name__ == "__main__"):
    escolher_jogo()