''' Implemente operadores sobrecarregados repr() e == para a classe Carta.
Sua nova classe Carta deverá se comportar como a seguir:
#>>> Carta('3', \u2660) == Carta('3', \u2660)
True
#>>> Carta('3', \u2660) == eval(repr(Carta('3', \u2660)))
True '''

class Carta:
    'representa uma carta com valor e naipe'

    # valores e naipes são variáveis da classe Baralho
    #valores = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}

    # naipes são 4 símbolos Unicode representando os 4 naipes
    #naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}

#Resolução
    def __init__(self, valor, naipe):
        'inicializa carta'
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return "Carta('{}','{}')".format(self.valor, self.naipe)

    def __eq__(self, other):
        return (self.valor == other.valor and self.naipe == other.naipe)


#Testes
a = Carta('3', 'a')
print(a == a)
print(a)
print(repr(a))
print(eval(repr(a)))
print(a == eval(repr(a)))