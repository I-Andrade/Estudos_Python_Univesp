'''
Problema Prático 10.4
Implemente o método recursivo pattern2(), que aceita um inteiro não negativo
 como entrada e exibe o padrão mostrado a seguir. Os padrões para as entradas
  0 e 1 são nada e um asterisco, respectivamente:

#>>> pattern2(0)
#>>> pattern2(1)
*

Os padrões para as entradas 2 e 3 aparecem em seguida.
#>>> pattern2(2)
*
**
*
#>>> pattern2(3)
*
**
*
***
*
**
*
'''

def asteR(n):
        if int(n)<0:
            print('Você não informou um inteiro não negativo. Rode o programa novamente...')
        else:
            if n == 0:
                print('')
            elif n == 1:
                print('*')
            else:
                asteR(n-1)
                print('*'*n)
                asteR(n-1)


teste = eval(input('Digite um número não negativo: '))
asteR(teste)


