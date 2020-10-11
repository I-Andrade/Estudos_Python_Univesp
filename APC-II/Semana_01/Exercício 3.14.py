#Implemente a função trocaPU(), que aceita uma lista como entrada e troca
# o primeiro e último elementos da lista. Você pode considerar que a lista
# não estará vazia. A função não deverá retornar nada.

def trocaPU(Lista):
    if Lista != []:
        tamanhoDaLista = len(Lista)
        Lista[0], Lista[tamanhoDaLista-1] = Lista[tamanhoDaLista-1], Lista[0]


#Testes

ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
#ingredientes = []
print(ingredientes)
trocaPU(ingredientes)
print(ingredientes)