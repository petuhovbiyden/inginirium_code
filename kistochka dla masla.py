import tkinter

def paint(event):
    canvas.create_oval(x-size, y-size, x+size, y+size, outline=color, fill=color)


def sizeble(event):
    global size, oval
    if event.keysym == 'Up' and size <= 99:
        size += 1
    elif event.keysym == 'Down' and size > 0:
        size -= 1
    label.config(text='size of brush' + str(size) + 'px')
    canvas.delete(oval)
    oval = canvas.create_oval(x-size, y-size, x+size, y+size, fill=color)

def mouse_pos(event):
    global x, y
    x = event.x
    y = event.y
    canvas.moveto(oval, x-size, y-size)

root = tkinter.Tk()
root.title('Kistochka dla masla')
size = 5
x, y = 0, 0
color = "#0FF"
label = tkinter.Label(root, text=f'size of brush {size} px')
label.pack()

canvas = tkinter.Canvas(root, bg='#FFF', width=640, height=640)
oval = canvas.create_oval(x-size, y-size, x+size, y+size, fill=color)
canvas.pack()
root.bind('<KeyPress>', sizeble)
root.bind('<Motion>', mouse_pos)
root.bind('<Button-1>', paint)

root.mainloop()
