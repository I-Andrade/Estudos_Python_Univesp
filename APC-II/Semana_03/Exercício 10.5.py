'''
Problema Prático 10.5

Implemente a função snowflake(), que aceita um inteiro não negativo n
 como entrada e exibe um padrão de floco de neve, combinando três curvas
  de Koch Kn desta maneira: quando a tartaruga terminar de desenhar a primeira
   e segunda curva de Koch, a tartaruga deverá girar 120 graus para a direita e
    começar a desenhar uma nova curva de Koch. Aqui, vemos a saída de snowflake(4).
'''

from turtle import Screen, Turtle

def snowflakes(n):
    'desenha flocos de neve com curvas de Koch usando instruções da função koch()'

    if int(n) < 0:
        print('Você não informou um inteiro não negativo. Rode o programa novamente...')
    else:
        def koch(n):
            'retorna direções turtle para desenhar a curva Koch(n)'
            if n == 0:  # caso básico
                return 'F'

            tmp = koch(n - 1)  # etapa recursiva: obtém direções para Koch(n – 1)
            # usa isso para construir direções para Koch(n)
            return tmp + 'L' + tmp + 'R' + tmp + 'L' + tmp

        def drawkoch(n):
            for move in directions:  # segue os movimentos especificados
                if move == 'F':
                    t.forward(300 / 3 ** n)  # move para frente, tamanho normalizado
                if move == 'L':
                    t.lt(60)  # gira 60 graus para a esquerda
                if move == 'R':
                    t.rt(120)  # gira 120 graus para a direita

        s = Screen()  # cria tela
        t = Turtle()  # cria turtle
        directions = koch(n)  # obtém direções para desenhar Koch(n)
        
        drawkoch(n)
        t.rt(120)
        drawkoch(n)
        t.rt(120)
        drawkoch(n)

teste = eval(input('Digite um número não negativo: '))
snowflakes(teste)
