from tkinter import Tk, Button, Label, Entry, END
from tkinter.messagebox import showinfo
from time import strftime, strptime
'''Problema Prático 9.4

Implemente uma variação do programa day.py, chamado day2.py. Em vez de exibir a mensagem do dia da semana em uma 
janela pop-up separada, insira-a na frente da data na caixa de entrada, conforme mostrado. Inclua também um botão
 rotulado com “Apagar”, que apaga a caixa de entrada.'''

def compute():
    'Comando para exibição do dia da semana a partir de uma data informada pelo usuário no Entry'
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    entry.insert(0,'{} '.format(weekday))

def clicked():
    global entry
    entry.delete(0, END)

root = Tk()

label = Label(root, text='Digite uma data: ')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button1 = Button(root, text='Enter', command=compute)
button1.grid(row=1, column=0)
button2 = Button(root, text='Clear', command=clicked)
button2.grid(row=1, column=1)
root.mainloop()