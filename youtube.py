import tkinter as tk
from tkinter import messagebox as mb

win = tk.Tk()

mylabel = Label(win , text = "名前を入力してください")
mylabel.pack()

text = Entry(win)
text.pack()
text.insert(END, " ")

def ok_click():
    a = text.get()
    mb.showinfo("Hi!!!",a + "さん、はじめまして！")

okButton = Button(win , text = "OK", command = ok_click)
okButton.pack()

win,mainloop()