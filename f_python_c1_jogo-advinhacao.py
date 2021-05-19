print("---------------------------------")
print("Bem vindo ao Jogo de Adivinhacao!")
print("---------------------------------")

num_sec = 28

chute = input("Por favor, digite um numero: ")

print("Voce digitou: ", chute)

num_convert = int(chute)

if(num_convert == num_sec):
  print("Voce acertou!")
else:
  print("Voce errou!")
  
  
print("Fim do Jogo!")