def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "dilminha"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")

        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}")
            index = index + 1
        print("jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
