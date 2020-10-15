'''
Modifique o construtor da classe Baralho de modo que a classe
também possa ser usada para jogos de carta que não usam o baralho
padrão de 52 cartas. Para esses jogos, precisaríamos oferecer a lista
de cartas explicitamente no construtor. Veja a seguir um exemplo um tanto artificial:

#>>> baralho = Baralho(['1', '2', '3', '4'])
#>>> baralho.shuffle()
#>>> baralho.distribuiCarta()
'3'
#>>> baralho.distribuiCarta()
'1'
'''


from random import shuffle
class Baralho:
    'representa um baralho de 52 cartas'

    # valores e naipes são variáveis da classe Baralho
    valores = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}

    # naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}

#Resolução
    def __init__(self, outrobaralho = []):
        'inicializa baralho de 52 cartas'
        self.baralho = outrobaralho
        if outrobaralho == []:
            for naipe in Baralho.naipes:  # naipes e valores são Baralho
                for valor in Baralho.valores:  # variáveis da classe
                    # inclui Carta com certo valor e naipe no baralho
                    self.baralho.append(self.Carta(valor, naipe))

    def Carta(self, valor, naipe):
        return valor + naipe

    def distribuiCarta(self):
        'distribui (remove e retorna) carta do topo do baralho'
        return self.baralho.pop()

    def shuffle(self):
        'mistura o baralho'
        shuffle(self.baralho)

#Testes
baralho = Baralho()
print(len(baralho.baralho))
baralho.shuffle()
print(baralho.baralho)
print(len(baralho.baralho))
print(baralho.distribuiCarta())
print(len(baralho.baralho))
print(baralho.distribuiCarta())
print(len(baralho.baralho))
print("")
baralho = Baralho(['1', '2', '3', '4'])
print(baralho.baralho)
baralho.shuffle()
print(baralho.baralho)
print(baralho.distribuiCarta())
print(baralho.distribuiCarta())