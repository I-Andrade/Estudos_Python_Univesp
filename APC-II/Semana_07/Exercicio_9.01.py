from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM, RIGHT, LEFT, BOTH
'''
Problema Prático 9.1
Escreva um programa peaceandlove.py que cria esta GUI:
O label de texto “Paz & Amor” deverá ser empurrado para a esquerda e ter um fundo preto com tamanho
 para caber 5 linhas de 20 caracteres. Se o usuário expandir a janela, o label deverá permanecer colado
  à borda esquerda da janela. A imagem do símbolo da paz deverá ser empurrada para a direita. Porém, quando
   o usuário expande a janela, o fundo branco deverá preencher o espaço criado. A figura mostra a GUI depois
    que o usuário a expandiu manualmente.
'''

root = Tk()

text = Label(master=root, font=("Courier", 18),
text='Paz & Amor',
             background='black',
             foreground='white',
             width=20,
             height=5)
text.pack(side=LEFT)

photo = PhotoImage(file='chefinho.gif').subsample(4,1)
image = Label(master=root, image=photo)
image.pack(side=RIGHT, expand=True, fill=BOTH)


root.mainloop()
