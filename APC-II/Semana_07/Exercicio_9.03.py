from tkinter import Tk, Button, Label, BOTTOM, TOP
from tkinter.messagebox import showinfo
from time import strftime, localtime, gmtime

def clicked(escolha):
    if escolha=='local':
        time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
        showinfo(message=time, title='Hora local')
    else:
        time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', gmtime())
        showinfo(message=time, title='Hora de Greenwich')

root = Tk()
root.title('Que horas são?')
root.geometry('400x50')
button1 = Button(root, text='Hora local', command=lambda: clicked('local'))
button2 = Button(root, text='Hora de Greenwich', command=lambda: clicked('gm'))
button1.pack(side=TOP)
button2.pack(side=BOTTOM)
root.mainloop()

