import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()
### 図形 ###
canvas.create_rectangle(100, 100, 120, 120, fill="red", tags="rect")
### 画像 ###
img = Image.open("smile.png")
tkimg = ImageTk.PhotoImage(img)
canvas.create_image(200, 200, image=tkimg, tags="img")
root.mainloop()