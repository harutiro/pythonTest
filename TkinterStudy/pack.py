import tkinter as tkinter

app = tkinter.Tk()
app.geometry("600x400")

canvas1 = tkinter.Canvas(
    app,
    width=100,
    height=50,
    bg="blue"
)

canvas2 = tkinter.Canvas(
    app,
    width=50,
    height=100,
    bg="green"
)

button1 = tkinter.Button(
    app,
    width=10,
    height=1,
    text="ボタン１"
)

button2 = tkinter.Button(
    app,
    width=5,
    height=2,
    text="ボタン\n２"
)


# 各ウィジェットの配置
canvas1.pack()
button1.pack()
button2.pack()
canvas2.pack()

app.mainloop()