import jogo_forca
import jogo_adivinhacao

print("\n***********************")
print("Escolha o jogo desejado")
print("***********************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual opção escolhida? "))

if(jogo == 1):
    print("Jogando forca")
elif(jogo ==2):
    print("Jogando adivinhação")