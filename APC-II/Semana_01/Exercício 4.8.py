#Escreva a função palavras() que aceita um argumento de entrada — um nome de arquivo —
# e retorna a lista de palavras reais (sem símbolos de pontuação !,.:;?) no arquivo.

def palavras(n):
    #Abrir e copiar o conteúdo do arquivo n.
    arquivo = open(n, 'r')
    conteudo = arquivo.read()
    arquivo.close()

    #Retirar os símbolos de pontuação.
    for p in ['!', ',', '.', ':', ';', '?']:
        conteudo = conteudo.replace(p, "")

   #Separar as palavras e imprimir
    listaPalavras = conteudo.split()
    print(listaPalavras)

#Teste
palavras('exercicio4.8.txt')