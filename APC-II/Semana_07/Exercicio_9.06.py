from tkinter import Tk, Canvas

'''Problema Prático 9.6

Implemente o programa draw2.py, uma modificação de draw.py,
 que aceita a exclusão da última curva desenhada na tela pressionando Ctrl
  e o botão esquerdo do mouse simultaneamente. Para fazer isso, você precisará
   excluir todos os segmentos de linha curtos criados por create_line() que compõem 
   a última curva. Isso, por sua vez, significa que você precisa armazenar todos os 
   segmentos que formam a última curva em algum tipo de contêiner.'''

# manipuladores de evento começam e desenham aqui
raiz = Tk()
oldx, oldy, movimentos = 0, 0, list()  # coordenadas do mouse (variáveis globais)


def begin(event):
    'inicializa o início da curva com a posição do mouse '
    global oldx, oldy
    oldx, oldy = event.x, event.y

def registra(id):
    movimentos.append(id)

def controlZ(event):
    if len(movimentos)!=0:
        canvas.delete(movimentos.pop())

def draw(event):
    'desenha um segmento de linha da posição antiga do mouse à nova'

    global oldx, oldy, canvas  # x e y serão mudados
    newx, newy = event.x, event.y  # nova posição do mouse

    # conecta posição anterior do mouse à atual
    identificador = canvas.create_line(oldx, oldy, newx, newy)
    registra(identificador)
    print()
    oldx, oldy = newx, newy  # nova posição torna-se a anterior

# canvas
canvas = Canvas(raiz, height=400, width=450)

# vincula evento de clique do botão esquerdo à função begin()
canvas.bind('<Button-1>', begin)
canvas.bind('<Control-Button-1>', controlZ)

# vincula evento de movimento do mouse enquanto o botão está pressionado
canvas.bind("<Button1-Motion>", draw)
canvas.pack()
raiz.mainloop()