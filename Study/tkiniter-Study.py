import tkinter as tk

root = tk.Tk()                # 窓を作る
root.title("Tkinterの練習")   # 窓のタイトルを設定
root.geometry("640x480")      # 窓の大きさを設定


x = 5

#キャンバスエリア
canvas = tk.Canvas(root, width = 400, height = 300)
rect = canvas.create_rectangle(x, 5, x+15, 20, fill = 'green')         # 四角形で塗りつぶし
canvas.place(x=0, y=0)          # キャンバスエリアを(0,0)で指定


def move(event=None):
    canvas.move(rect, 10, 0)
    canvas.after(500,move)

#===========================================ラベル
Static1 = tk.Label(text=u'test')
Static1.pack()
static2 = tk.Label(text=u'test', foreground='#ff0000', background='#ffaacc')
static2.pack()

# 任意の場所に配置したい場合は，
# Static1.place(x=x座標, y=y座標)



#===========================================エントリー
EditBox = tk.Entry(width=50)
EditBox.insert(tk.END,"挿入する文字列")
EditBox.pack()

#ここで，valueにEntryの中身が入る
value = EditBox.get()

#エントリーの中身を削除
EditBox.delete(0, tk.END)


#===========================================ボタン
Button = tk.Button(text=u'ボタンです', width=50)
Button.pack()


Button.bind("<Button-1>",move) 
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド






root.mainloop()
