from tkinter import Tk, Text, BOTH

def key_pressed(event):
    'Imprime o caractere digitado no teclado'
    print('char: {}'.format(event.keysym))

def mouse_clicked_left(event):
    'Informa que foi clicado com o botão esquerdo do mouse'
    print('mouse left clicked')

def mouse_clicked_right(event):
    'Informa que foi clicado com o botão direito do mouse'
    print('mouse right clicked')

root = Tk() # Cria a janela
text = Text(root, width=20, height='5') #Cria o texto na janela root.

# Associa eventos às funções -> bind()
text.bind('<KeyPress>', key_pressed)
text.bind('<Button-1>', mouse_clicked_left)
text.bind('<Button-3>', mouse_clicked_right)

# Empacota
text.pack(expand=True, fill=BOTH)

#Executa
root.mainloop()