import forca
import advinhacao

def escolhe_jogo():
    print("********************************")
    print("escolha o seu jogo!")
    print("********************************")

    print("(1) forca (2) advinhacao")

    jogo = int(input("qual o jogo?"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando advinhacao")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()