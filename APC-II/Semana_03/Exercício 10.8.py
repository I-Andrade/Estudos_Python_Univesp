'''
Problema Prático 10.8

Implemente a função frequent2(), que usa um dicionário para calcular
 a frequência de cada item na lista de entrada e retorna o item que ocorre
  com mais frequência. Depois, realize um experimento e compare os tempos de execução
   de frequent() e frequent2() em uma lista obtida usando a função buildInput(),
    definida no Problema Prático 10.7.
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


def frequent1(lst): # função retirada do livro
    '''retorna item que ocorre com mais frequência
    na lista lst não vazia'''
    if lst == []:
        print("Informar uma lista com itens")
    else:
        lst.sort()  # primeiro classifica lista

        currentLen = 1  # tamanho da sequência atual
        longestLen = 1  # tamanho da sequência mais longa
        mostFreq = lst[0]  # item com sequência mais longa

        for i in range(1, len(lst)):
            # compara item atual com anterior
            if lst[i] == lst[i - 1]:  # se igual
                # sequência atual continua
                currentLen += 1
            else:  # se não igual
                # atualiza sequência mais longa, se necessário
                if currentLen > longestLen:  # se sequência que terminou
                                             # for a maior até aqui
                    longestLen = currentLen  # armazena seu tamanho
                    mostFreq = lst[i - 1]       # e o item
                # inicia nova sequência
                currentLen = 1
        return mostFreq

def frequent2(lst): # Necessita de melhorias
    'retorna frequência dos itens em listaItens'

    if lst == []:
        print("Informar uma lista com itens")
    else:
        contadores = {}  # inicializa dicionário de contadores
        for item in lst:
            if item in contadores:  # contador para o item já existe
                contadores[item] += 1  # portanto, incrementa
            else:  # contador para item é criado
                contadores[item] = 1  # e inicializado em 1
        contadores
        listaValores = dict.values(contadores)
        maiorContador = max(listaValores)
        for item in contadores:
            if contadores[item] == maiorContador:
                itemMaisFrequente = item
        return itemMaisFrequente


#Registrando os testes
print('------------------------------')
timingAnalysis(frequent1,20000,80001,20000,10)
print('------------------------------')
timingAnalysis(frequent2,20000,80001,20000,10)
print('------------------------------')



#Resolução
print('Comparando os tempos de execução verificamos que utilização do dicionário é mais rápida.')

