'''
No Capítulo 5, implementamos a função fatorial() iterativamente.
A função fatorial n! tem uma definição recursiva natural:
n!   =   1    se n = 0
                 n · (n− 1)!     se n > 0
Reimplemente a função fatorial() usando a recursão.
Além disso, estime quantas chamadas à fatorial() são feitas para algum valor de entrada n > 0.
'''

def fatorialR(n):
        if int(n)<0:
            print('Você não informou um inteiro não negativo. Rode o programa novamente...')
        else:
            if n < 2:
                return 1
            else:
                return n * fatorialR(n-1)


teste = eval(input('Digite um número não negativo: '))
teste = fatorialR(teste)
print(teste)

