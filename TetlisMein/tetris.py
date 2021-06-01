import tkinter as tk
from tkinter.constants import Y
import random
import numpy as np
# pip install numpy



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
        blocks = []

        # print(self.shape)

        if(self.shape == 0):
            blocks = [Block(-1,0),Block(0,0),Block(0,-1),Block(1,0),]
        elif(self.shape == 1):
            blocks = [Block(-1,-1),Block(0,-1),Block(0,0),Block(1,0),]
        elif(self.shape == 2):
            blocks = [Block(-1,0),Block(0,0),Block(0,-1),Block(1,-1),]
        elif(self.shape == 3):
            blocks = [Block(-1,-2),Block(-1,-1),Block(-1,0),Block(0,0),]
        elif(self.shape == 4):
            blocks = [Block(0,-2),Block(0,-1),Block(-1,0),Block(0,0),]
        elif(self.shape == 5):
            blocks = [Block(-1,-1),Block(-1,0),Block(0,0),Block(0,-1),]
        elif(self.shape == 6):
            blocks = [Block(-2,0),Block(-1,0),Block(0,0),Block(1,0),]
        

        

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
    
    def putBlock(self, x, y):
        self.tiles[y][x] = 1

    def findLineFilled(self):
        for y in range(21):
            print(self.tiles[y])
            isFilled = all( t == 1 for t in self.tiles[y])
            if isFilled :
                return y
        return -1

    def cutLine(self, y):
        self.tiles = np.delete(self.tiles, y, 0)
        self.tiles = np.insert(self.tiles , 0, [1,0,0,0,0,0,1,0,0,0,0,1] , axis=0)

        print(self.tiles)

    
    def tileAt(self,x,y):
        return self.tiles[y][x]

class Game(tk.Frame) :
    def __init__ (self,master = None):
        super().__init__(master)
        self.master = master

        self.minoVx = 0
        self.minoVr = 0
        self.minoDrop = False
        self.mino = self.makeMino()
        self.field = Field()
        self.fc = 0

        self.speed = 0
        self.kotei = 0

        self.master.bind("<Left>",self.leftController) #左矢印キー
        self.master.bind("<Right>",self.rightController) #右矢印キー
        self.master.bind("<Key-e>",self.eKeyController) 
        self.master.bind("<Key-q>",self.qKeyController) 
        # self.master.bind("<Down>",self.downController) #下矢印キー

    def makeMino(self):
        return Mino(5,10,0,random.randint(0,6))

    def isMinoMovable(self, mino, field):
        blocks = mino.calcBlocks()
        
        # print(mino.x)
        # print(mino.y)

        # BAG: Falseしか出ない。
        # for b in blocks:
            # print("x" + str(b.x))
            # print("y" + str(b.y))
            # print(field.tileAt(b.x,b.y))
            
        return all( field.tileAt(b.x + mino.x , b.y + mino.y) == 0 for b in blocks)

    def proc(self):

        # 落下
        if(self.minoDrop or self.fc %20 == 19):
            futureMino = self.mino.copy()
            futureMino.y += 1

            # Debag.hyouzi(self,self.field)

            if(self.isMinoMovable(futureMino,self.field)):
                self.mino.y += 1
            else:#固定化
                if self.kotei == 2:
                    for b in self.mino.calcBlocks():
                        self.field.putBlock(b.x + self.mino.x, b.y + self.mino.y)

                    self.mino = self.makeMino()
                    self.kotei = 0

                else:
                    self.kotei += 1


            # 消去
            
            while self.field.findLineFilled() != -1:
                
                self.field.cutLine(self.field.findLineFilled())
            self.minoDrop = False


        # 横操作
        if(self.minoVx != 0):
            futureMino = self.mino.copy()
            futureMino.x += self.minoVx

            # print(futureMino.x)
            # print(futureMino.y)
            Debag.hyouzi(self,self.field)

            if(self.isMinoMovable(futureMino,self.field)):
                self.mino.x += self.minoVx

            self.minoVx = 0

        # 回転
        if(self.minoVr != 0):
            futureMino = self.mino.copy()
            futureMino.rot += self.minoVr

            # print(futureMino.x)
            # print(futureMino.y)
            # Debag.hyouzi(self,self.field)

            if(self.isMinoMovable(futureMino,self.field)):
                self.mino.rot += self.minoVr

            self.minoVr = 0

        canvas.delete("all")
        self.mino.draw()
        self.field.draw()
        self.fc += 1

        print(self.speed)

        global jobid
        jobid = self.after(8, self.proc)


        
        

        

    def leftController(self,event): #左矢印キーが押されたら
        self.minoVx = -1

    def rightController(self,event): #右矢印キーが押されたら
        self.minoVx = 1

    def eKeyController(self,event):
        self.minoVr = 1
    
    def qKeyController(self,event):
        self.minoVr = -1

    # def downController(self,event): #下矢印キーが押されたら
        

class Debag ():

    def hyouzi(self,field):

        for y in range(22):
            for x in range(12):
                print(field.tileAt(x,y) , end = "")
            
            print()
    






jobid = None





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

