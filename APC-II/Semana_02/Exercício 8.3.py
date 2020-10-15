"""
Implemente a classe Retângulo, que representa retângulos.
A classe deverá implementar estes métodos:
•setTamanho(largura, comprimento):
    aceita dois valores numéricos como entrada e define o comprimento e largura do retângulo.
•perímetro(): retorna o perímetro do retângulo.
•área(): retorna a área do retângulo.
#>>> retângulo = Retângulo(3,4)
#>>> retângulo.perímetro()
14
#>>> retângulo.área()
12
"""

# Resolução
class Retangulo:
    'Classe que representa retangulos'
    l = 0
    c = 0

    def __init__(self, largura, comprimento):
        if (type(largura) in [int, float]) and (type(comprimento) in [int, float]) and (largura > 0) and (comprimento > 0):
            self.l = largura
            self.c = comprimento
            print('Você criou um retângulo com as seguintes dimensões: {} x {}.'.format(self.l, self.c))
        else:
            print('ERRO: Valores informados: {} e {}.'.format(largura, comprimento))
            print('Por favor informar apenas valores numéricos maiores do que 0 nos argumentos.\n')

    def setTamanho(self, largura, comprimento):
        'Define tamanho dos lados do retangulo'
        if (type(largura) in [int, float]) and (type(comprimento) in [int, float]) and (largura > 0) and (comprimento > 0):
            self.l = largura
            self.c = comprimento
            print('Você modificou o retângulo para as seguintes dimensões: {} x {}'.format(self.l, self.c))
        else:
            print('ERRO: Valores informados: {} e {}.\n'.format(largura, comprimento))
            print('Por favor informar apenas valores numéricos maiores do que 0 nos argumentos.')


    def perimetro(self):
        'Define o perimetro do retangulo'
        if (self.l != 0 ) and (self.c != 0):
            return ('Perímetro = ' + str((self.l)*2 + (self.c)*2))
        else:
            return "Você tentou calcular o perímetro, mas os lados do retangulo ainda não foram totalmente definidos.\n"

    def area(self):
        'Define a área do retangulo'
        if (self.l != 0) and (self.c != 0):
            return ('Área = ' + str((self.l)*(self.c)))
        else:
            return "Você tentou calcular a área, mas os lados do retangulo ainda não foram totalmente definidos.\n"

# Teste
retangulo = Retangulo(0,0)
print(retangulo.perimetro())
print(retangulo.area())
retangulo.setTamanho(2.5, 7)
print(retangulo.perimetro())
print(retangulo.area())
help(Retangulo)