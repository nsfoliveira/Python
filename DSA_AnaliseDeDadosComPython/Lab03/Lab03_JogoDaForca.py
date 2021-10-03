# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 15:05:02 2021

@author: Natalia
"""

# Hangman Game - Jogo da Forca
# Utilizanod conceitos aprendidos de Programação orientada a Objetos

# import
import random

# Tabuleiro
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Criando a classe
class Forca:

    # método construtor:
    def __init__(self, word):

    # método para advinhar a letra:
    def guess(self, letter):

    # método para verificar se o jogo já terminou:
    def hangman_over(self):

    # método para verificar se o jogador venceu:
    def hangman_won(self):

    # método para não mostrar a letra no board:
    def hide_word(self):

    # método para checar o status do game e imprimir o board na tela
    def print_game_status(self):

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
       print('\nGame over! Você perdeu.')
       print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
main()

