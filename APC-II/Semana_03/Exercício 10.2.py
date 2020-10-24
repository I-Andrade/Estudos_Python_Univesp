'''
Use o pensamento recursivo para implementar a função recursiva saúde() que, sobre a
 entrada inteira n, exibe n strings 'Hip ' seguidos por Hurrah.

#>>> cheers(0)
Hurrah!!!

#>>> cheers(1)
Hip Hurrah!!!

#>>> cheers(4)
Hip Hip Hip Hip Hurrah!!!

O caso básico da recursão deverá ser quando n é 0;
 sua função deverão, então, exibir Hurrah. Quando n > 1,
  sua função deverá exibir 'Hip ' e depois chamar recursivamente
   a si mesma sobre a entrada inteira n – 1.
'''

def saude(n):
        if int(n)<0:
            print('Você não informou um inteiro não negativo. Rode o programa novamente...')
        else:
            if n == 0:
                print('Hurrah!!!')
            else:
                print('Hip', end=' ')
                saude(n-1)

teste = eval(input('Digite um número não negativo: '))
saude(teste)

