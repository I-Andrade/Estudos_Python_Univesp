from tkinter import Tk, Button, Label, Entry, END
from tkinter.messagebox import showinfo
from time import strftime, strptime

def compute():
    'Comando para exibição do dia da semana a partir de uma data informada pelo usuário no Entry'
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))
    entry.delete(0, END)

root = Tk()
label = Label(root, text='Digite uma data: ')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='Enter', command=compute)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()