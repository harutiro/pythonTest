import tkinter as tk



root = tk.Tk()
root.geometry('400x400')
root.title("カウントアップ")

num = 0

def puraDousa (event=None):
    global num
    
    num += 1
    numMoji["text"] = str(num)

# ===========================================

numMoji = tk.Label(text=u'0',font=("",20))
numMoji.pack(anchor='center',expand=1)

pura = tk.Button(text=u'+1',width=10)
pura.pack(side=tk.BOTTOM)
pura.bind("<Button-1>",puraDousa)

root.mainloop()

