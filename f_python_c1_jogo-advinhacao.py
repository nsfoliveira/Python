print("---------------------------------")
print("Bem vindo ao Jogo de Adivinhacao!")
print("---------------------------------")

num_sec = 28
tentativas = 3

while(tentativas > 0):
  chute = input("Por favor, digite um numero: ")
  print("Voce digitou: ", chute)
  num_convert = int(chute)
  acertou = num_convert == num_sec
  maior   = num_convert > num_sec
  menor   = num_convert < num_sec

  if(acertou):
     print("Voce acertou!")
  else:
    if(maior):
      print("Voce errou! O seu chute foi maior que o numero secreto")
  elif(menor):
        print("Voce errou! O seu chute foi menor que o numero secreto")
  tentativas = tentativas - 1
    
print("Fim do Jogo!")