import glbl
import funcs
from tkinter import *

root = Tk()
def create_board():
    
    for i in range(3):
        for j in range(3):
            glbl.Buttons[i].append(Button(root, text = '-', width = 10, height = 10,command = lambda i=i,j=j: funcs.player_move(i,j)))
            glbl.Buttons[i][j].grid(row = i, column = j)




