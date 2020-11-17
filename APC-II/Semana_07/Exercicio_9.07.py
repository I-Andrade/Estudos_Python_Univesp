from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

'''Problema Prático 9.7

Complete a implementação das funções down(), left() e right() no programa plotter.py.'''

# manipuladores de evento up(), down(), left() e right()
def up():
    'move caneta 10 pixels para cima'
    global y, canvas                  # y é modificado
    canvas.create_line(x, y, x, y-10)
    y -= 10

def down():
    'move caneta 10 pixels para baixo'
    global y, canvas                  # y é modificado
    canvas.create_line(x, y, x, y+10)
    y += 10

def left():
    'move caneta 10 pixels para esquerda'
    global x, canvas                  # x é modificado
    canvas.create_line(x, y, x-10, y)
    x -= 10

def right():
    'move caneta 10 pixels para direita'
    global x, canvas                  # x é modificado
    canvas.create_line(x, y, x+10, y)
    x += 10

raiz = Tk()
# tela com borda de tamanho 200 x 200

canvas = Canvas(raiz, height=200, width=200, relief=SUNKEN, borderwidth = 3)
canvas.pack(side=LEFT)

# frame para manter os 4 botões
box = Frame(raiz)
box.pack(side=RIGHT)

# os 4 widgets de botão têm a caixa do widget Frame como seu master
button = Button(box, text='up', command=up)
button.grid(row=0, column=0, columnspan=2)

button = Button(box, text='left', command=left)
button.grid(row=1, column=0)

button = Button(box, text='right', command=right)
button.grid(row=1, column=1)

button = Button(box, text='down', command=down)
button.grid(row=2, column=0, columnspan=2)

x, y = 100, 100  # posição da caneta, inicialmente no meio
raiz.mainloop()