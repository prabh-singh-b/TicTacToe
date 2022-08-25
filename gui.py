import glbl
import funcs
from tkinter import *

def create_board(root):
    
    for i in range(3):
        for j in range(3):
            glbl.Buttons[i].append(Button(root, text = '-', width = 10, height = 10,command = lambda i=i,j=j: funcs.move(i,j)))
            glbl.Buttons[i][j].grid(row = i, column = j)




