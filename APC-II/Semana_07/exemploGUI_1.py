from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM


root = Tk()
photo = PhotoImage(file='chefinho.gif').subsample(5)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18),
text='Olá alunos da UNIVESP!')
text.pack(side=BOTTOM)
root.mainloop()

