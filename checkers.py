import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='#FFF', width=400, height=400)
for i in range(0, 400, 50):
    canvas.create_line((i, 0),  (i, 400), fill='#000')
    canvas.create_line((0, i),  (400, i), fill='#000')
for i in range(8):
    for j in range(3):
        if (i+j) % 2:
            canvas.create_oval(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill="#FFF")
    for j in range(5,8):
        if (i+j) % 2:
            canvas.create_oval(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill="#FFF")

canvas.pack()
win.mainloop()
