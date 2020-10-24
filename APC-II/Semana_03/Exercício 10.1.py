'''
Implemente o método recursivo reverse(), que aceita um inteiro
não negativo como entrada e exibe os dígitos de n verticalmente,
começando com o dígito de ordem baixa.
#>>> reverse(3124)
4
2
1
3
'''

def reverse1(n):
    if int(n)<0:
        print('Você não informou um inteiro não negativo. Rode o programa novamente...')
    else:
        n = str(n)
        i = len(n)
        if i == 1:  # caso básico: Imprime ultimo caractere.
            print(n[i-1])
        else:  # etapa recursiva: Imprime ultimo caractere direita e o exclui para proxima etapa recursiva.
            print(n[i-1])
            reverse1(n[:-1])

def reverse2(n):
    if n<0:
        print('Você não informou um inteiro não negativo. Rode o programa novamente...')
    else:
        if n < 10:  # etapa recursiva: Imprime ultimo caractere direita e o exclui para proxima etapa recursiva.
            print(n)
        else:
            print(n%10)
            reverse2(n//10)


teste = eval(input('Digite um número não negativo: '))
print("Usando reverse1:")
reverse1(teste)
print("Usando reverse2:")
reverse2(teste)