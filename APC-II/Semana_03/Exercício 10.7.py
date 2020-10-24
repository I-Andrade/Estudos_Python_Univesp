'''
Usando um experimento, analise o tempo de execução das funções dup1(),
 dup2(), dup(3) e dup(4). Você deverá testar cada função nas 10 listas
  de tamanho 2000, 4000, 6000 e 8000, obtidas por:

import random
def buildInput(n):
   'retorna uma lista de n inteiros aleatórios no intervalo [0, n**2]'
    res = []
    for i in range(n):

        res.append(random.choice(range(n**2)))
    return res

Observe que a lista retornada por essa função é obtida escolhendo repetidamente
 n números no intervalo de 0 a n2 – 1 e pode ou não conter duplicatas.
  Ao terminar, comente os resultados.
'''

import random
import time

def buildInput(n):
    'retorna uma lista de n inteiros aleatórios no intervalo [0, n**2]'
    res = []
    for i in range(n):
        res.append(random.choice(range(n**2)))
    return res

def timing(func, n):
    'roda func sobre entrada retornada por buildInput'
    funcInput = buildInput(n)  # obtém entrada para func

    start = time.time()  # toma hora inicial
    func(funcInput)  # roda func sobre funcInput
    end = time.time()  # toma hora final
    return end - start  # retorna tempo de execução

def timingAnalysis(func, start, stop, inc, runs):
    '''exibe tempos de execução médios da função func sobre entradas
       de tamanho start, start+inc, start+2*inc, … até stop '''

    for n in range(start, stop, inc):  # para cada tamanho de entrada n
        acc = 0.0  # inicializa acumulador
        for i in range(runs):  # repete runs vezes:
            acc += timing(func, n)  # roda func sobre entrada de tamanho n
            # e acumula tempos de execução
            # exibe tempos de execução médios para tamanho de entrada n
        formatStr = 'Tempo de execução de {}({}) é {:.20f} segundos.'
        print(formatStr.format(func.__name__, n, acc / runs))


def dup1(lst):
    'retorna True se lista lst tiver duplicatas; caso contrário, False'
    for item in lst:
        if lst.count(item) > 1:
            return True
    return False

def dup2(lst):
    'retorna True se lista lst tiver duplicatas; caso contrário, False'
    lst.sort()
    for index in range(1, len(lst)):
        if lst[index] == lst[index-1]:
            return True
    return False


def dup3(lst):
    'retorna True se lista lst tiver duplicatas, caso contrário, False'
    s = set()
    for item in lst:
        if item in s:
            return False
        else:
            s.add(item)
    return True

def dup4(lst):
    'retorna True se lista lst tiver duplicatas, caso contrário, False'
    return len(lst) != len(set(lst))

#Registrando os testes
print('------------------------------')
timingAnalysis(dup1,2000,8001,2000,10)
print('------------------------------')
timingAnalysis(dup2,2000,8001,2000,200)
print('------------------------------')
timingAnalysis(dup3,2000,8001,2000,200)
print('------------------------------')
timingAnalysis(dup4,2000,8001,2000,200)
print('------------------------------')


#Resolução
print('Comparando os tempos de execução verificamos que a busca linear é a mais lenta')
print('comparada com a  busca linear ordenada (3ª mais rápida), dicionário (2ª + rápida) e conjunto (a + rápida).')
