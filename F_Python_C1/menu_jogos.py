import jogo_forca
import jogo_adivinhacao
print("***********************")
print("Escolha o jogo desejado")
print("***********************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual opção escolhida? "))

if(jogo == 1):
    print("Jogando forca")
    jogo_forca.jogar()
elif(jogo ==2):
    print("Jogando adivinhação")
    jogo_adivinhacao.jogar()
