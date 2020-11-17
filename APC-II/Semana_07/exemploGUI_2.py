from tkinter import Tk, Label, RAISED

root = Tk()
labels = [['1', '2', '3'],
['4', '5', '6'],
['7', '8', '9'],
['*', '0', '#']]
for r in range(4):
    for c in range(3):
        label2 = Label(root, relief=RAISED, padx=50, pady=50, text=labels[r][c], font=('Arial', 35))
        label2.grid(row=r, column=c)
root.mainloop()