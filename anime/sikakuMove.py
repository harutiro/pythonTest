import  tkinter as tk
import time

root = tk.Tk()
root.geometry('400x400')
root.title('canvasの使い方')

#図形を壁画するキャンバスをウインド上に作成
canvas=tk.Canvas(root,width=300,height=300,bg="white")
canvas.pack()

#図形の壁画
dx=20
dy=20
square=canvas.create_rectangle(5,5,5+dx,5+dy,fill='red')#四角

x=150#四角の初期x座標
y=150#四角の初期y座標

while True:
    # Coords そのアイテムIDの図形を指定した文だけ変形をしていく。
    # ID、左上のX座標、左上のY座標、右下のｘ座標、右下のｙ座標
    canvas.coords(square,x,y,x+dx,y+dy)
    y += 1
    
    time.sleep(0.02) #0.02秒ずつ更新
    root.update() #ウインド画面を更新

root.mainloop()