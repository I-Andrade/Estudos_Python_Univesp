'''
Implemente a função contaPalavra(), que aceite como entrada um texto
 — como uma string — e exiba a frequência de cada palavra no texto.
 Você pode considerar que o texto não possui pontuação e que as
 palavras são separadas por espaços em branco.

#>>> texto = 'all animals are equal but some \
animals are more equal than others'

#>>> contaPalavra(texto)
all      appears 1 time.
animals  appears 2 times.
some     appears 1 time.
equal    appears 2 times.
but      appears 1 time.
are      appears 2 times.
others   appears 1 time.
than     appears 1 time.
more     appears 1 time.
'''

#dados:

texto = 'all animals are equal but some \
animals are more equal than others'
print('Texto: ' + texto)
print('')

#função:      (houve melhoria na função, parte anterior desconsiderada por comentário.
def contaPalavra(texto): #valorAtual = 0): # n = número de consultas sequênciais na lista
    contador = dict()
    palavrasSeparadas = str.split(texto)
    for palavra in palavrasSeparadas:
        if palavra in contador:
            #valorAtual = contador.get(estudantes[i])
            #valorAtual += 1
            contador[palavra] += 1  #= valorAtual
        else:
            contador[palavra] = 1
    for palavra in contador:
        print('{:<11} appears {} time(s)'.format(palavra, contador.get(palavra)))


#testes:
contaPalavra(texto)