print("********************************")
print("Bem Vindo ao jogo de Advinhação!")
print("********************************")

num_secreto = 28
total_tentativa = 3

while(total_tentativa > 0):
    print("\nNúmero de tentativas possíveis: ", total_tentativa)
    chute = input("Digite seu chute: ")
    print("Você digito: ", chute)
    chute_convert = int(chute)

    acertou = chute_convert == num_secreto
    maiorq  = chute_convert > num_secreto
    menorq  = chute_convert < num_secreto
    
    if(acertou):
        print("Você acertou!")
    else:
        if(maiorq):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menorq):
            print("Você errou! Seu chute foi menor que o número secreto")

    total_tentativa = total_tentativa - 1

print("Fim do Jogo!")