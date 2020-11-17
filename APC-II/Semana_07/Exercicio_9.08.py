from tkinter import Tk, Text, BOTH, Frame

'''Problema Prático 9.8

Reimplemente a aplicação GUI keylogger.py como uma nova classe de widget definida pelo usuário.
 Você precisará decidir se é necessário atribuir o widget Text contido nessa GUI a uma variável
  de instância ou não.'''

class Keylogger(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        text = Text(self, width=20, height=5)

        # Vincula evento de tecla à função de tratamento de evento record()
        text.bind('<KeyPress>', self.record)
        text.pack(expand=True, fill=BOTH)

    def record(self, event):
        '''função de manipulação de evento para evento de tecla pressionada
           evento de entrada é do tipo tkinter.Event '''
        print('char = {}'.format(event.keysym))  # exibe símbolo da tecla



root = Tk()
root.geometry('200x200')
key = Keylogger(root)
key.pack()
root.mainloop()


