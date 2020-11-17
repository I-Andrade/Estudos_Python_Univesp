from tkinter import Tk, Label, RAISED
from calendar import monthrange
'''
Problema Prático 9.2

Implemente a função cal() que aceita como entrada um ano e um mês (um número entre 1 e 12)
e começa com uma GUI que mostra o calendário correspondente. Por exemplo, o calendário mostrado é obtido usando:
>>> cal(2012, 2)

Para fazer isso, você precisará calcular (1) o dia da semana (segunda, terça,…) referente
ao primeiro dia do mês e (2) o número de dias no mês (levando em consideração os anos bissextos). 
A função monthrange(), definida no módulo calendar, retorna exatamente esses dois valores:

>>> from calendar import monthrange
>>> monthrange(2012, 2)   # ano 2012, mês 2 (fevereiro)
(2, 29)

O valor retornado é uma tupla. O primeiro valor na tupla, 2, corresponde à quarta-feira
(segunda é 0, terça é 1 etc.). O segundo valor, 29, é o número de dias em fevereiro no ano 2012, um ano bissexto.
'''

def cal(ano, mes):

    diaDaSemanaEQuantidadeDeDias = monthrange(ano, mes)
    diaDaSemana = diaDaSemanaEQuantidadeDeDias[0]
    quantidadeDeDias = diaDaSemanaEQuantidadeDeDias[1]
    if diaDaSemana==0 and quantidadeDeDias==28:
        matriz = [['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], ['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
    elif (diaDaSemana==6 and quantidadeDeDias==30) or (diaDaSemana>4 and quantidadeDeDias==31):
        matriz = [['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],['','','','','','',''], ['','','','','','',''], ['','','','','','',''], ['','','','','','',''], ['','','','','','',''], ['','','','','','','']]
    else:
        matriz = [['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],['','','','','','',''], ['','','','','','',''], ['','','','','','',''], ['','','','','','',''], ['','','','','','','']]

    ultimoDiaDaSemanaFoi = 0
    for semana in range(1,len(matriz)):
        ultimoDiaDaSemanaFoi += 1
        for dia in range(ultimoDiaDaSemanaFoi,32):
            matriz[semana][diaDaSemana] = dia
            diaDaSemana +=1
            if diaDaSemana==7:
                diaDaSemana=0
                ultimoDiaDaSemanaFoi = dia
                break
            if dia==quantidadeDeDias:
                break


    root = Tk()
    root.title("Year: {}, Month: {}".format(ano,mes))
    for r in range(len(matriz)):
        for c in range(7):
            label = Label(root, width=4, height=2, text=matriz[r][c], font=('Arial', 35))
            label.grid(row=r, column=c)
    root.mainloop()



#Testes
cal(2020, 11    )
