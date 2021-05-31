import tkinter as tk
from tkinter.constants import Y
import time



class Block :
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        s = 25
        square=canvas.create_rectangle(s*self.x , s*self.y , self.x*s+s, self.y*s+s ,fill='red')#四角




class Mino:
    def __init__(self, x, y, rot, shape):
        self.x = x
        self.y = y
        self.rot = rot
        self.shape = shape

    def calcBlocks(self) -> list:
        blocks = [
            Block(-1,0),
            Block(0,0),
            Block(0,-1),
            Block(1,0),
        ]

        

        rot = (40000000 + self.rot) % 4

        for r in range(rot):
            for i,b in enumerate(blocks):
                blocks[i] = Block(-b.y,b.x)

        return blocks

    def draw(self):

        blocks = self.calcBlocks()

        for b in blocks:
            b.x += self.x
            b.y += self.y
            b.draw()



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
        for y in range(22):
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

        root.after(1000,game.proc())


#ウインドを作成
root=tk.Tk()
root.geometry('400x600')
root.title('Tetlis')

canvas=tk.Canvas(root,width=400,height=600,bg="white")
canvas.pack()


game = Game()

Mino(4,15,3,0).draw()

root.after(1000,game.proc())





root.mainloop()

