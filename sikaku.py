import tkinter as tk

root = tk.Tk()                # 窓を作る
root.title("Tkinterの練習")   # 窓のタイトルを設定
root.geometry("640x480")      # 窓の大きさを設定


x = 5

#キャンバスエリア
canvas = tk.Canvas(root, width = 400, height = 300)

rect = canvas.create_rectangle(x, 5, x+15, 20, fill = 'green')         # 四角形で塗りつぶし

canvas.place(x=0, y=0)          # キャンバスエリアを(0,0)で指定

def move():
    canvas.move(rect, 10, 0)
    canvas.after(500,move)

root.mainloop()
