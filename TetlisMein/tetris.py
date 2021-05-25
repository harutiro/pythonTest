import tkinter as tk
from tkinter.constants import Y
import time

#ウインドを作成
root=tk.Tk()
root.geometry('400x600')
root.title('Tetlis')

canvas=tk.Canvas(root,width=400,height=600,bg="white")
canvas.pack()

class Block :
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        s = 25
        square=canvas.create_rectangle(s*self.x , s*self.y , s, s ,fill='red')#四角




class Mino:
    def __init__(self, x, y, rot, shape):
        self.x = x
        self.y = y
        self.rot = rot
        self.shape = shape

    def calcBlocks(self):
        blocks = [
            Block(-1,0),
            Block(0,0),
            Block(0,-1),
            Block(1,0),
        ]

        rot = (40000000 + self.rot) % 4

        for r in range(rot):
            for b in blocks:
                Block(-b.y,b.x)

    def draw(self):
        blocks = Mino

        for b in blocks.calcBlocks:
            b.x += self.x
            b.y += self.y
            b.drow()



class Field:
    def __init__(self):
        self.tiles = [
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1],
        ]

    def draw(self):
        for y in range(21):
            for x in range(12):
                if self.tileAt(x,y) == 0:
                    continue
                Block(x,y).draw()
    
    
    def tileAt(self,x,y):
        return self.tiles[y][x]

class Game :
    def __init__ (self):
        self.mino = Mino(5,10,0,0)
        self.field = Field()
        self.fc = 0

    def proc(self):
        self.mino.draw()
        self.field.draw()
        self.fc += 1


game = Game()
while True:
    game.proc()
    time.sleep(0.016) #0.02秒ずつ更新


root.mainloop()

