#Implemente a função olimpíadas(t), que faz com que a tartaruga t desenhe os anéis olímpicos
#mostrados a seguir. Use a função jump() do módulo ch3.

import turtle
def jump(t, x, y):
    # 'faz tartaruga saltar para coordenadas (x, y)'
    t.penup()
    t.goto(x, y)
    t.pendown()

def olimpiada(t):
    # 'faz tartaruga criar os arcos olimpicos coloridos'
    t.pensize(7)
    cor = ['blue', 'yellow', 'black', 'green', 'red']
    arco, x, y = 0, 110, -100
    for arco in range(0,5):
        t.pencolor(cor[arco])
        if arco % 2 == 0:
         jump(t, x*arco, y)
        else:
            jump(t, x*arco, y*2)
        t.circle(100)

#Teste

s = turtle.Screen() 
t = turtle.Turtle()
olimpiada(t)