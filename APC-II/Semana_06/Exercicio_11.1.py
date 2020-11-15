from urllib.request import urlopen

'''Escreva o método news() que aceita um URL de um site Web de notícias
e uma lista de tópicos de notícias (ou seja, strings) e calcula o número
 de ocorrências de cada tópico nas notícias.

#>>> news('http://bbc.co.uk',['economy','climate','education'])
economy appears 3 times.
climate appears 3 times.
education appears 1 times.
'''

#Definindo o método...

def news(url, listaTopicos):
    abreDadosDaUrl = urlopen(url)
    print(type(abreDadosDaUrl))
    html = abreDadosDaUrl.read().decode().lower()

    for topico in listaTopicos:
      contagem = html.count(topico)
      print("{} appears {} time(s)".format(topico, contagem))

#Definindo a lista para testes e a URL
listaTopicos = ['futebol','clima','eleições', 'covid']
url = 'https://www.uol.com.br/'

#testes:
news(url,listaTopicos)

