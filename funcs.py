from tkinter import DISABLED
import glbl

def check_win(moves):
    for i in glbl.win_cond:
        count = 0
        for j in i:
            if j in moves:
                count += 1
        if count == 3:
            return True
    return False

def move(i,j):
    
    glbl.Buttons[i][j].config(text = "O")
    glbl.Buttons[i][j].config(state = DISABLED)
    glbl.player_moves.append((i*3)+j+1)
    print(check_win(glbl.player_moves))