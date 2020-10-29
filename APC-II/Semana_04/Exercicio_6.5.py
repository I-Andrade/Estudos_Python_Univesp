'''
Use a função lookup()para implementar uma aplicação de pesquisa de agenda.
 Sua função aceita, como entrada, um dicionário representando uma agenda.
  No dicionário, as tuplas contendo nomes e sobrenomes de indivíduos (as chaves)
   são mapeadas a strings contendo números de telefone (os valores). Veja aqui um exemplo:

#>>> agenda = {('Anna','Karenina'):'(123)456-78-90',
              ('Yu', 'Tsun'):'(901)234-56-78',
              ('Hans', 'Castorp'):'(321)908-76-54'}

Sua função deverá oferecer uma interface simples com o usuário,
 por meio da qual ele possa informar o nome e sobrenome de um indivíduo
  e obter o número de telefone atribuído a esse indivíduo.

#>>> lookup(agenda)
Digite o nome: Anna
Digite o sobrenome: Karenina
(123)456-78-90
Digite o nome: Yu
Digite o sobrenome: Tsun
(901)234-56-78
'''

#dicionário  com  chave tupla:

agenda = {('Anna','Karenina'):'(123)456-78-90',
              ('Yu', 'Tsun'):'(901)234-56-78',
              ('Hans', 'Castorp'):'(321)908-76-54'}

#função:
def lookup(agenda, chave1='', chave2='', chave = tuple()):
    print('Bem vindo à função "lokkup".')
    print('Quando quiser encerrar a função, digite "Sair" nos campos abaixo.')
    print('')
    while (chave1 and chave2) != 'Sair':
      chave1 = str(input('Digite o nome:  '))
      chave2 = str(input('Digite o sobrenome:  '))
      print('')
      chave = (chave1, chave2)
      if chave in agenda:
        print(agenda[chave])
        print('')
      elif (chave1 and chave2) != 'Sair':
        print('O número informado não está em uso.')
        print('')
    print('Agradecemos por usar nossa função.')


#testes:
lookup(agenda)

