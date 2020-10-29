'''Escreva uma função estadoNasc() que aceite como entrada o nome completo de um presidente
  dos Estados Unidos (como uma string) e retorne o estado em que ele nasceu.
  Você deverá usar esse dicionário para armazenar o estado em que cada presidente recente nasceu:

{'Barack Hussein Obama II':'Hawaii',

 'George Walker Bush':'Connecticut',

 'William Jefferson Clinton':'Arkansas',

 'George Herbert Walker Bush':'Massachussetts',

 'Ronald Wilson Reagan':'Illinois',

 'James Earl Carter, Jr':'Georgia'}

#>>> estadoNasc('Ronald Wilson Reagan')

'Illinois'

'''

#dicionário:

dicionario = {'Barack Hussein Obama II':'Hawaii',

 'George Walker Bush':'Connecticut',

 'William Jefferson Clinton':'Arkansas',

 'George Herbert Walker Bush':'Massachussetts',

 'Ronald Wilson Reagan':'Illinois',

 'James Earl Carter, Jr':'Georgia'}

#função:
def estadoNasc(nomeDoPresidente):
    return dicionario[nomeDoPresidente]

#testes:
teste = estadoNasc('George Walker Bush')
print(teste)
teste = estadoNasc('James Earl Carter, Jr')
print(teste)