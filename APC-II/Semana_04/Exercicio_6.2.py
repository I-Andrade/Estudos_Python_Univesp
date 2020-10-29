'''Implemente a função rlookup(), que oferece o recurso de pesquisa reversa de uma agenda de telefones.
 Sua função aceita, como entrada, um dicionário representando uma agenda de telefones.
 No dicionário, os números de telefone (chaves) são mapeados para indivíduos (valores).
 Sua função deverá oferecer uma interface de usuário simples, por meio da qual
  um usuário pode inserir um número de telefone e obter o nome e sobrenome do indivíduo atribuído a esse número.

#>>> agenda_r = {'(123)456-78-90':['Anna','Karenina'],
                '(901)234-56-78':['Yu', 'Tsun'],

                '(321)908-76-54':['Hans', 'Castorp']}

#>>> rlookup(agenda_r)

Digite número do telefone no formato (xxx)xxx-xx-xx: (123)456-78-90
('Anna', 'Karenina')

Digite número do telefone no formato (xxx)xxx-xx-xx: (453)454-55-00
O número informado não está em uso.

Digite número do telefone no formato (xxx)xxx-xx-xx:
'''

#dicionário:

dicionario = {'(123)456-78-90':['Anna','Karenina'],
              '(901)234-56-78':['Yu', 'Tsun'],
              '(321)908-76-54':['Hans', 'Castorp']}

#função:
def rlookup(dicionario, chave=''):
    print('Bem vindo à função "rlokkup".')
    print('Quando quiser encerrar a função, digite "Sair" ')
    print('')
    while chave != 'Sair':
      chave = str(input('Digite número do telefone no formato (xxx)xxx-xx-xx:  '))
      print('')
      if chave in dicionario:
        print(dicionario[chave])
        print('')
      elif chave != 'Sair':
        print('O número informado não está em uso.')
        print('')
    print('Agradecemos por usar nossa função.')


#testes:
rlookup(dicionario)

