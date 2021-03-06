# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:02:51 2021

@author: cschm
"""

from IPython.display import clear_output

# Create the board for tic-tac-toe

def display_board(board):
    
    clear_output
    print('_____')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('_____')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('_____')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
# Pick which person goes first
def player_input():
    
    marker = ''
    
    # We need to keep asking player 1 to choose either X or O
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, please choose X or O: ').upper()
        
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return(player1,player2)
    # Whatever player 1 choose, player 2 will be the opposite marker.

# Place marker on the correct position
def place_marker(board, marker, position):
    
    board[position] = marker
    
# Verify if someone won the game    
def win_check(board, mark):
    
   
    return((board[1] == board[2] == board[3] == mark) or #Row1
    (board[4] == board[5] == board[6] == mark) or #Row2
    (board[7] == board[8] == board[9] == mark) or #Row3
    (board[1] == board[4] == board[7] == mark) or #Column1
    (board[2] == board[5] == board[8] == mark) or #Column2
    (board[3] == board[6] == board[9] == mark) or #Column3
    (board[1] == board[5] == board[9] == mark) or #Diagonal1
    (board[3] == board[5] == board[7] == mark)) #Diagonal2
    
# Decides who goes first
import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Check if space is available
def space_check(board, position):
    
    return board[position] == '*'

# Check if the board is full
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    # Board is full if this function returns True
    return True

# Make sure the player only picks a position between 1-9
def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        
    return position

# Ask the player if they want to play again
def replay():
    
    choice = input('Play again? Enter Yes or No?')
    
    return choice == 'Yes'

# Code to actually run the game

print('Welcome to Tic Tac Toe!')

while True:

    # Game Play
    
    # Start - board set-up
    
    the_board = ['*']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? Yes or No? ')
    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place marker
            place_marker(the_board,player1_marker,position)
            # Check if won, tie, or lose
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 Wins!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie')
                    break
                else:
                    turn = 'Player 2'
                    
                    # if not, next player's turn
        else:
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place marker
            place_marker(the_board,player2_marker,position)
            # Check if won, tie, or lose
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 Wins!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie')
                    break
                else:
                    turn = 'Player 1'
                    

    
    if not replay():
        break
