import tkinter as tk
import random

#ウインドを作成
root=tk.Tk()
root.geometry('400x400')
root.title('じゃんけんゲーム')


# ======================================動作部分

judge = ["あいこ", "負け", "勝ち"]
hands = ["グー", "チョキ", "パー"]



def hantei(zibun=0):
    run = random.randint(0,2)

    aiteKekka["text"] = hands[run]

    i = (zibun-run+3)%3

    return i




def guuDousa(event=None):
    zibunKekka["text"] = "グー"
    kekka["text"] = judge[hantei(0)]

def paDousa(event=None):
    zibunKekka["text"] = "パー"
    kekka["text"] = judge[hantei(2)]

def tyoDousa(event=None):
    zibunKekka["text"] = "チョキ"
    kekka["text"] = judge[hantei(1)]


# =====================================画面部分
aiteMoji = tk.Label(text=u'相手')
aiteMoji.pack()
aiteKekka = tk.Label(text=u'じゃんけん')
aiteKekka.pack()

zibunKekka = tk.Label(text=u'')
zibunKekka.pack(side=tk.BOTTOM)
zibunMoji = tk.Label(text=u'自分')
zibunMoji.pack(side=tk.BOTTOM)


kekka = tk.Label(text=u'結果', font=("",20))
kekka.pack(anchor='center',expand=1)

dx = 65
guu = tk.Button(text=u'グー', width=10)
guu.place(x=dx,y=250)
guu.bind("<Button-1>",guuDousa)

pa = tk.Button(text=u'パー', width=10)
pa.place(x=dx+100,y=250)
pa.bind("<Button-1>",paDousa)

tyo = tk.Button(text=u'チョキ', width=10)
tyo.place(x=dx+200,y=250)
tyo.bind("<Button-1>",tyoDousa)







root.mainloop()