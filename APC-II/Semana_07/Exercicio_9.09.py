from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT
'''Problema Prático 9.9

Reimplemente a aplicação GUI plotter como uma classe de widget definida pelo usuário,
 que encapsula o estado da plotter (ou seja, a posição da caneta). Pense cuidadosamente
  sobre quais widgets precisam ser atribuídas a variáveis de instância.'''

class Plotter(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        #variáveis de instância
        self.x, self.y = 100, 100  # posição da caneta, inicialmente no meio
        self.canvas = Canvas(raiz, height=200, width=200, relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        # frame para manter os 4 botões
        box = Frame(raiz)
        box.pack(side=RIGHT)

        # os 4 widgets de botão têm a caixa do widget Frame como seu master
        button = Button(box, text='up', command=self.up)
        button.grid(row=0, column=0, columnspan=2)

        button = Button(box, text='left', command=self.left)
        button.grid(row=1, column=0)

        button = Button(box, text='right', command=self.right)
        button.grid(row=1, column=1)

        button = Button(box, text='down', command=self.down)
        button.grid(row=2, column=0, columnspan=2)



    # manipuladores de evento up(), down(), left() e right()
    def up(self):
        'move caneta 10 pixels para cima'
        self.canvas.create_line(self.x, self.y, self.x, self.y-10)
        self.y -= 10

    def down(self):
        'move caneta 10 pixels para baixo'
        self.canvas.create_line(self.x, self.y, self.x, self.y+10)
        self.y += 10

    def left(self):
        'move caneta 10 pixels para esquerda'
        self.canvas.create_line(self.x, self.y, self.x-10, self.y)
        self.x -= 10

    def right(self):
        'move caneta 10 pixels para direita'
        self.canvas.create_line(self.x, self.y, self.x+10, self.y)
        self.x += 10



raiz = Tk()
plotter = Plotter(raiz)
plotter.pack()
raiz.mainloop()