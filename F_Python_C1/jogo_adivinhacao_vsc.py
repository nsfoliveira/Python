print("********************************")
print("Bem Vindo ao jogo de Advinhação!")
print("********************************")

num_secreto = 28
total_tentativa = 3
rodada  = 1

while(rodada <= total_tentativa):
    print("\nTentativa ", rodada, " de ", total_tentativa)
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

    rodada = rodada + 1

print("\nFim do Jogo!!\n")