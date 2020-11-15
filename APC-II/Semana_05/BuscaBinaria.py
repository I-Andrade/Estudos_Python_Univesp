def busca_binaria(l, x, inicio, fim):
    meio = (inicio + fim) // 2

    if fim < inicio:
        return print("Elemento {} não encontrado na lista".format(x))

    if x == l[meio]:
        return meio

    if x < l[meio]:
        return busca_binaria(l, x, inicio, meio-1)

    if x > l[meio]:
        return busca_binaria(l, x, meio+1, fim)


## TESTES
lista = [9, 5, 8, 6]
print(lista)
lista.sort()
print(lista)
print("Procurando 5")
print("Elemento 5 encontrado, está na posição {}".format(busca_binaria(lista, 5, 0, len(lista)-1)))
print("")

lista = [9, 5, 8, 3, 6]
print(lista)
lista.sort()
print(lista)
print("Procurando 6")
print("Elemento 6 encontrado, está na posição {}".format(busca_binaria(lista, 6, 0, len(lista)-1)))
print("")

print("Procurando 2")
print(busca_binaria(lista, 2, 0, len(lista)-1))
print("")