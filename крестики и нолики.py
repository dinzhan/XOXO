import random
import time

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

dictionary = {'center':4, 'center-left':3,
              'center-right':5, 'center-up':1,
              'center-left-up':0, 'center-right-up':2,
              'center-right-down':8, 'center-left-down':6,
              'center-down':7}

def show_board():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])

def isFree(pos):
    if board[pos] != 'X' and board[pos] != 'O':
        return True
    else:
        return False

def computer():
    random_position = random.randint(0, 8)
    if isFree(random_position) == True:
        board[random_position] = comp
    else:
        computer()
        
def isWin(choice):
    if (board[0] == board[1] == board[2] == choice or
        board[3] == board[4] == board[5] == choice or
        board[6] == board[7] == board[8] == choice or
        board[0] == board[3] == board[6] == choice or
        board[1] == board[4] == board[7] == choice or
        board[2] == board[5] == board[8] == choice or
        board[0] == board[4] == board[8] == choice or
        board[2] == board[4] == board[6] == choice):
        return True
    else:
        return False

def isDraw():
    for element in board:
        if element != 'X' or element != 'O':
            continue

        if isWin(me) == False or isWin(comp) == False:
            return True
        else:
            return False
        


    
show_board()
me = input('Choose X or O: ').upper()
if me == 'X':
    comp = 'O'
else:
    comp = 'X'

while True:
    while True: 
        position = 0 # для числового обозначения позиции (индекса)
        position_word = input('Choose the position:\ncenter\ncenter-left\ncenter-right\ncenter-up\ncenter-left-up\ncenter-right-up\ncenter-down\ncenter-left-down\ncenter-right-down: ').lower()
        for key, value in dictionary.items():
            if key == position_word:
                position = value # фиксируем позицию, которую выбрал пользователь
        
        if isFree(position) == True: # если позиция свободна
            board[position] = me # то ставим на позицию x или o
            break
    show_board()
    if isWin(me) == True:
        print('Game over. You have won!')
        break
    computer()
    print('Computer is thinking . . .')
    time.sleep(3)
    show_board()
    if isWin(comp) == True:
        print('Game over! Computer has won!')
        break
    if isDraw() == True:
        print('Draw!')
        break
    
