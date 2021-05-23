print("\n********************************")
print("Bem Vindo ao jogo de Advinhação!")
print("********************************")

num_secreto = 28
total_tentativa = 3
rodada  = 1

for rodada in range(1, total_tentativa + 1):
    print("\nTentativa {} de {}".format(rodada, total_tentativa)) #string interpolation
    chute = input("Digite um número de 1 a 100: ")
    
    print("Você digito: ", chute)
    chute_convert = int(chute)

    if(chute_convert < 1 or chute_convert > 100):
        print("Número Inválido. Você deve digitar um número de 1 a 100")
        continue #ele não quebra o laço

    chute_convert = int(chute)
    acertou = chute_convert == num_secreto
    maiorq  = chute_convert > num_secreto
    menorq  = chute_convert < num_secreto
    
    if(acertou):
        print("Você ganhou!!")
        break #parar o laço quando acertar
    else:
        if(maiorq):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menorq):
            print("Você errou! Seu chute foi menor que o número secreto")


print ("\nNúmero Secreto é {}".format(num_secreto))
print("\nFim do Jogo!!\n")