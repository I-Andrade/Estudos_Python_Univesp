'''
Implemente a função sync() que aceita uma lista de agendas
 (em que cada agenda é um conjunto de números de telefone)
  como entrada e retorna uma agenda (como um conjunto) contendo a união de todas as agendas.

#>>> agenda4 = {'234-56-78', '456-78-90'}
#>>> agendas = [agenda1, agenda2, agenda3, agenda4]
#>>> sync(agendas)
{'234-56-78', '456-78-90', '123-45-67', '345-67-89'}
'''

#conjuntos (set):
agenda1 = {'345-67-89', '456-78-90'}
agenda2 = {'123-45-67',}
agenda3 = {'234-56-78', '456-78-90'}
agenda4 = {'234-56-78', '456-78-91'}
agendas = [agenda1, agenda2, agenda3, agenda4]

#função:
def sync(agendas, conjuntoDeAgendas = set()):
    print('Bem vindo à função "sync".')
    print('')
    for agenda in agendas:
        conjuntoDeAgendas = conjuntoDeAgendas | agenda
    print('Conjunto união das agendas: ' )
    return print(conjuntoDeAgendas)


#testes:
sync(agendas)

