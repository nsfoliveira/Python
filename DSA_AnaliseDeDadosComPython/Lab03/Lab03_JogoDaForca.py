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
        self.word = word
        self.missed_letters = [] # criando lista para as letras erradas
        self.guessed_letters = [] # criando lista para as letras certas

    # método para advinhar a letra:
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # método para verificar se o jogo já terminou:
    def hangman_over(self):
        return seld.hangman_won() or (len(self.missed_letters) == 6) # se ganhou ele chama o método hangman_won, \
        # se não ele verificar se o comprimento da lista é igual a 6 e se for verdadeiro acabou o jogo

    # método para verificar se o jogador venceu:
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # método para não mostrar a letra no board:
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)]) # para não precisar colocar a posição do indice da lista, usando o \
        # comprimento da lista de lestras errada
        print('\nPalavra: ' + self.hide_word())
        print('\nLetra errada: ',)
        for letter in self.missed_letters:
            print(letter,)
        print()
        print('Letras corretas: ',)
        for letter in self.guessed_letters:
            print(letter,)
        print()
# Método para ler uma palavra de forma aleatório do banco de palavra (arquivo txt)
def rand_word():
    with open('palavra.txt', rt) as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

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

