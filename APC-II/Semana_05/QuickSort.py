#### Os print comentados foram inseridos para compreensão do método durante os testes.

def quick_sort(v, ini, fim):
    # print("Início QUICK SORT")
    meio = (ini + fim) // 2
    pivo = v[meio]
    i = ini
    j = fim
    # print("Inicio {} Fim {} Meio {} Pivô {} Indice 'i' {} Indice 'j' {} ".format(ini, fim, meio, pivo, i, j))

    while i < j:
        # print("#####Caso que i < j ({} < {})".format(i,j))
        while v[i] < pivo:
            # print("Como v[i] {} < {} pivo".format(v[i], pivo))
            # print("i recebe mais um: {}".format(i+1))
            i += 1

        while v[j] > pivo:
            # print("Como v[j] {} > {} pivo".format(v[j], pivo))
            # print("j recebe menos um: {}".format(j-1))
            j -= 1

        if i <= j:
            # print("Caso que indice 'i' é menor ou igual ao 'j'")
            # print("Inverte v[i] com v[j]")
            v[i], v[j] = v[j], v[i]
            # print("Lista em ordenação {}".format(v))

        # print("'i' recebe mais 1, passa valer {}".format(i+1))
        i += 1
        # print("'j' recebe menos 1, passa valer {}".format(j-1))
        j -= 1
        # print("##############FIM do método, antes das chamadas recursivas")
        # print("")
    if j > ini:
        # print("#### Chamando recursivamente QUICK SORT quando j > inicio")
        quick_sort(v, ini, j)
    if i < fim:
        # print("#### Chamando recursivamente QUICK SORT quando i < fim")
        quick_sort(v, i, fim)

## TESTES
lista = ['C', 'A2', 'S', 'A1']
print("Lista desordenada: ")
print(lista)
print("")
quick_sort(lista, 0, len(lista) - 1)
print("Lista ordenada pelo QUICK SORT: ")
print(lista)