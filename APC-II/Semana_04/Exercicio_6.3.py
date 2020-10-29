'''Desenhe o estado dos contadores depois de visitar os próximos
três nomes na lista estudantes. Faça um desenho depois de visitar
 'Adam', outro depois de visitar o segundo 'Adam' e ainda outro depois
  de visitar 'Jimmy', usando a Figura 6.3 como seu modelo.
'''

#lista de estudantes:

estudantes = ['Cindy', 'John', 'Cindy', 'Adam', 'Adam',
                  'Jimmy', 'Joan', 'Cindy', 'Joan']

#função:      (houve melhoria na função, parte anterior desconsiderada por comentário.
def frequencia(n): #valorAtual = 0): # n = número de consultas sequênciais na lista
    contador = dict()
    for i in range(0, n):
        if estudantes[i] in contador:
            #valorAtual = contador.get(estudantes[i])
            #valorAtual += 1
            contador[estudantes[i]] += 1  #= valorAtual
        else:
            contador[estudantes[i]] = 1
    return print(contador)


#testes:
print("Desenho da contagem até 4º elemento da lista estudantes: ")
frequencia(4)
print('')
print("Desenho da contagem até 5º elemento da lista estudantes: ")
frequencia(5)
print('')
print("Desenho da contagem até 6º elemento da lista estudantes: ")
frequencia(6)
print('')

