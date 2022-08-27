from random import Random
from tkinter import DISABLED
import glbl
import random

def check_win(moves):
    for i in glbl.win_cond:
        count = 0
        for j in i:
            if j in moves:
                count += 1
        if count == 3:
            return 1
    if (len(glbl.player_moves)+ len(glbl.cpu_moves)) == 9:
        return 0

    return -1

def player_move(i,j):
    move(i,j,'O')
    glbl.player_moves.append((i*3)+j+1)

    res = check_win(glbl.player_moves)
    if res == 1:
        print('Player has won the Game')
        return
    elif res == 0:
        print('The game has ended in a draw')
        return
    else:
        cpu_move()

def move(i,j,txt = 'O'):
    glbl.Buttons[i][j].config(text = txt)
    glbl.Buttons[i][j].config(state = DISABLED)

def cpu_move():
    x = 0
    while True:
        x = random.randint(0,8)
        if(not (x+1 in glbl.player_moves or x+1 in glbl.cpu_moves)):
            glbl.cpu_moves.append(x+1)
            break
    print(f'{x=}')
    i,j = x//3,x%3
    move(i,j,txt = 'X')
    # res = check_win
    # if res == 1:
