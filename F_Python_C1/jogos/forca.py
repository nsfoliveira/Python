def jogar ():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "Dilminha"
    letras_acertadas = ["_","_","_","_","_","_","_","_",]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip()  # para tratar a variável caso tenha espaços

        index = 0  # posicionador

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()): #convertendo as variaveis em maiusculas
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
