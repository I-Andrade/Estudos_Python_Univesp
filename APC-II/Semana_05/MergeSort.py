#### Os print comentados foram inseridos para compreensão do método durante os testes.

def merge_sort(v, ini, fim):
    # print("################Dentro do método MERGE: ")
    # print("Início: " + str(ini))
    # print("Fim: " + str(fim))
    if ini < fim:
        meio = (ini + fim) // 2
        # print("Meio: " + str(meio))
        # print("Chamando MERGE recursivamente pela ESQUERDA")
        merge_sort(v, ini, meio)
        # print("Chamando MERGE recursivamente pela DIREITA")
        merge_sort(v, meio+1,fim)
        intercala(v, ini, meio,fim)

def intercala(v, ini, meio, fim):
    # print("################Dentro do método INTERCALA: ")
    # print("Início: " + str(ini))
    # print("Meio: " + str(meio))
    # print("Fim: " + str(fim))
    L = v[ini:meio+1] #vetor auxiliar ESQUESDA
    R = v[meio+1:fim+1] #vetor auxiliar DIRETA
    L.append(999) #sentinela VALOR MAXIMO
    R.append(999) #sentinela VALOR MAXIMO
    i = 0 #Ponteiro de indice do vetor L
    j = 0 #Ponteiro de indice do vetor R
    for k in range(ini, fim+1):
        # print("K é igual a: " + str(k))
        # print("Lista L: " + str(L))
        # print("Lista R: " + str(R))
        # print("Comparando {} com {}".format(L[i],R[j]))
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
        # print("Lista em ordenação:" + str(v) )
    # print("")


## TESTES
lista = [9,5,8,6]
print("Lista desordenada: ")
print(lista)
merge_sort(lista,0,len(lista)-1)
print("Lista ordenada pelo MERGE SORT: ")
print(lista)