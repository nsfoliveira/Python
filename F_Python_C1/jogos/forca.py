def jogar ():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "dilminha"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip()  # para tratar a variável caso tenha espaços

        index = 0  # posicionador

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()): #convertendo as variaveis em maiusculas
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print("jogando...")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
