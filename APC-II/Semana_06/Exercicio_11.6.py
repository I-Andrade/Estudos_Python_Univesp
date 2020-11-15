from re import findall

'''
Problema Prático 11.6

Desenvolva a função frequency(), que toma uma string como entrada,
 calcula a frequência de cada palavra na string e retorna um dicionário que mapeia
  palavras na string à sua frequência. Você deverá usar uma expressão regular 
  para obter a lista de todas as palavras na string.

>>> content = 'The pure and simple truth is rarely pure and never\
         simple.'

>>> frequency(content)

{'and': 2, 'pure': 2, 'simple': 2, 'is': 1, 'never': 1,
'truth': 1, 'The': 1, 'rarely': 1}
'''

def frequencyRE(string):
    dicionario = dict()
    listaComPalavras = findall('[a-zA-Z]+', string)

    for palavra in listaComPalavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1

    return dicionario

# Testes
content = 'The pure and simple truth is rarely pure and never simple.'
print(content)
dicionario = frequencyRE(content)
print(dicionario)