'''Implemente a classe Vetor, que aceita os mesmos métodos da classe Ponto
que desenvolvemos na Seção 8.4.
A classe Vetor também deverá aceitar a adição de vetor e operações de produto.
A adição de dois vetores:
#>>> v1 = Vetor(1, 3)
#>>> v2 = Vetor(-2, 4)
é um novo vetor cujas coordenadas são a soma das coordenadas correspondentes de v1 e v2:
#>>> v1 + v2
Vetor(-1, 7)
O produto de v1 e v2 é a soma dos produtos das coordenadas correspondentes:
#>>> v1 * v2
10
Para que um objeto Vetor seja exibido como Vetor (. , .) em vez de Ponto(. , .),
 você precisará redefinir o método _ _repr_ _().'''
class Point:
    'classe que representa pontos no plano'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, coordx):
        'define coordenada x do ponto como coordx'
        self.x = coordx

    def sety(self, coordy):
        'define coordenada y do ponto como coordy'
        self.y = coordy

    def get(self):
        'retorna tupla com coordenadas x e y do ponto'
        return (self.x, self.y)

    def move(self, dx, dy):
        'muda as coordenadas x e y por dx e dy'
        self.x += dx
        self.y += dy

        def __repr__(self):
            return 'Ponto ( {}, {} )'.format(self.x, self.y)

# Resolução

class Vetor(Point):
    'classe que representa vetores e extende a classe Point'

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def __repr__(self):
        return 'Vetor ( {}, {} )'.format(self.x, self.y)

# Teste
v1 = Vetor(1, 3)
v2 = Vetor(-2, 4)
print(v1)
print(v2)
print(v1 + v2)
print(v1 * v2)