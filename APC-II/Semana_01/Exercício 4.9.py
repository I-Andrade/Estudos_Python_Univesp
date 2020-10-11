#Implemente a função meuGrep(), que toma como entrada duas strings,
# um nome de arquivo e uma string alvo,
# e exibe cada linha do arquivo que contém a string alvo como uma substring.

def meuGrep(n, alvo):
    #Abrir e copiar o conteúdo do arquivo n em uma lista.
    arquivo = open(n, 'r')
    conteudo = arquivo.readlines()
    arquivo.close()

    #Imprimir as linhas que contêm o alvo.
    for p in conteudo:
        if (p.__contains__(alvo)):
            print(p)

#Teste
meuGrep('exercicio4.9.txt', 'above')