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

    def copy(self):
        return Mino(self.x, self.y, self.rot, self.shape)



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

class Game(tk.Frame) :
    def __init__ (self,master = None):
        super().__init__(master)
        self.master = master

        self.minoVx = 0
        self.mino = Mino(5,10,0,0)
        self.field = Field()
        self.fc = 0

        self.master.bind("<Left>",self.leftController) #左矢印キー
        self.master.bind("<Right>",self.rightController) #右矢印キー
        # self.master.bind("<Down>",self.downController) #下矢印キー

    def isMinoMovable(self, mino, field):
        blocks = mino.calcBlocks()
        print("Go")
        return all( field.tileAt(b.x,b.y) == 0 for b in blocks)

    def proc(self):

        if(self.minoVx != 0):
            futureMino = self.mino.copy()
            futureMino.x += self.minoVx
            game = Game
            print("Redy")
            if(game.isMinoMovable(self,futureMino,self.field)):
                print("OK")
                self.mino.x += self.minoVx

            self.minoVx = 0

        canvas.delete("all")
        self.mino.draw()
        self.field.draw()
        self.fc += 1

        self.after(16,self.proc)

    def leftController(self,event): #左矢印キーが押されたら
        self.minoVx = -1

    def rightController(self,event): #右矢印キーが押されたら
        self.minoVx = 1

    # def downController(self,event): #下矢印キーが押されたら
        












#ウインドを作成
root=tk.Tk()
root.geometry('400x600')
root.title('Tetlis')

canvas=tk.Canvas(root,width=400,height=600,bg="white")
canvas.pack()


game = Game(master = root)
game.proc()


# Mino(4,15,3,0).draw()

# root.after(1000,game.proc())





root.mainloop()

