'''
Usando a aplicação de análise do tempo de execução, desenvolvida nesta seção, analise o tempo de execução das funções power() e rpower(), bem como o operador embutido **. Você fará isso executando timingAnalysis() sobre as funções power2(), rpower2() e pow2(), definidas a seguir, e usando tamanhos de entrada de 20 mil a 80 mil, com incrementos de 20 mil.
def power2(n):
    return power(2,n)
def rpower2(n):
    return rpower(2,n)
def pow2(n):
    return 2**n
Quando terminar, discuta qual técnica o operador embutido ** provavelmente utiliza.
'''

import time

def buildInput(n):
    'retorna entrada para funções'
    return n

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
        formatStr = 'Tempo de execução de {}({}) é {:.7f} segundos.'
        print(formatStr.format(func.__name__, n, acc / runs))


def power(a, n):
    'retorna a à potência n '
    res = 1
    for i in range(n):
        res *= a
    return res

def rpower(a, n):
    'retorna a à potência n '
    if n == 0:  # caso básico: n == 0
        return 1
    tmp = rpower(a, n // 2)  # etapa recursiva: n > 0
    if n % 2 == 0:
        return tmp * tmp  # a**n = a**(n//2) * a**a(n//2)
    else:  # n % 2 == 1
        return a * tmp * tmp  # a**n = a**(n//2) * a**a(n//2) * a

def power2(n):
    return power(2,n)

def rpower2(n):
    return rpower(2,n)

def pow2(n):
    return 2**n

#Registrando os testes
print('------------------------------')
timingAnalysis(power2,20000,80001,20000,1)
print('------------------------------')
timingAnalysis(rpower2,20000,80001,20000,1)
print('------------------------------')
timingAnalysis(pow2,20000,80001,20000,1)
print('------------------------------')

#Resolução
print('Comparando os tempos de execução é evidente que provavelmente o operador ** utiliza-se de função recursiva')
