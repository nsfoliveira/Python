import forca
import adivinhacao
print("\n***********************")
print("Escolha o jogo desejado")
print("***********************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual opção escolhida? "))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo ==2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
