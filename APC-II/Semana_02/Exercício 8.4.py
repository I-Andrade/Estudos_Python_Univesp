"""
Modifique a classe Animal que desenvolvemos na seção anterior
de modo que aceite um construtor com dois, um ou nenhum argumento de entrada:
#>>> snoopy = Animal('cão', 'latir')
#>>> snoopy.fala()
Eu sou um cão e sei latir.
#>>> tweety = Animal('canário')
#>>> tweety.fala()
Eu sou um canário e sei emitir sons.
#>>> animal = Animal()
#>>> animal.fala()
Eu sou um animal e sei emitir sons.
"""

#Resolução
class Animal:
    'representa um animal'

    def __init__(self, especie='animal', linguagem='emitir sons'):
        'Construtor que recebe os argumentos especie e linguagem'
        self.esp = especie
        self.ling = linguagem


    def setEspecie(self, especie):
        'define a espécie do animal'
        self.esp = especie


    def setLinguagem(self, linguagem):
        'define a linguagem do animal'
        self.ling = linguagem

    def fala(self):
        ' exibe uma sentença pelo animal'
        print('Eu sou um {} e sei {}'.format(self.esp, self.ling))

#Testes
snoopy = Animal('cão', 'latir')
snoopy.fala()

tweety = Animal('canário')
tweety.fala()

animal = Animal()
animal.fala()

animal.setEspecie('gato')
animal.setLinguagem('miar')
animal.fala()