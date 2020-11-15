from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

#usamos a função urlopen() para solicitar e receber um documento HTML hospedado em um servidor Web
response = urlopen('http://www.w3c.org/Consortium/facts.html')

print(type(response))

#o método geturl() de HTTPResponse retorna o URL do recurso solicitado
print(response.geturl())

#Para obter todos os cabeçalhos de resposta HTTP, você pode usar o método getheaders()
for header in response.getheaders():
    print(header)
print()
#o método read() retorna um objeto do tipo bytes.
#Isso porque os recursos abertos por urlopen() poderiam muito bem ser arquivos de áudio ou vídeo (ou seja, arquivos binários)

html = response.read()
print(type(html))
print()
#Se o recurso for um arquivo HTML (ou seja, um arquivo de texto),
# faz sentido decodificar a sequência de bytes em caracteres Unicode
# que eles representam.Usamos o método decode() da classe bytes
html = html.decode()
print(html)
print()

#Podemos manipular as strings agora:
print(html.count('Web'))

#Com tudo o que aprendemos até aqui, podemos escrever uma função que aceita um URL
# de uma página Web como entrada e retorna o conteúdo do arquivo-fonte da página Web como uma string:

def getSource(url):
    'returns the content of resource specified by url as a string'
    response = urlopen(url)
    html = response.read()
    return html.decode()

decodificado = getSource('https://www.uol.com.br/')
print(decodificado)

#HTMLParser
parser = HTMLParser()
parser.feed(html)

#HTMLParser com metodos personalizados através de herança
class LinkParser(HTMLParser):
    '''' analisador de doc. HTML que mostra valores dos
        atributos href nas tags de início de âncora'''
    def handle_starttag(self, tag, attrs):
        'mostra valor do atributo href, se houver'
        if tag == 'a':  # se tag de âncora
        # procura atributo href e mostra seu valor
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

linkparser = LinkParser()
linkparser.feed(html)

# O módulo urllib.parse da Biblioteca Padrão Python
# oferece alguns métodos que operam sobre URLs, incluindo um que faz exatamente o que queremos, o método urljoin()
url = 'http://www.w3.org/Consortium/mission.html'
relative = '/Consortium/contact.html'
absoluto = urljoin(url, relative)
print(absoluto)
print()

# Usando o urljoin()
class Collector(HTMLParser):
    'coleta URLs de hyperklink em uma lista'

    def __init__(self, url):
        'inicializa analisador, o URL e uma lista'
        HTMLParser.__init__(self)
        self.url = url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        'coleta URLs de hyperlink em sua forma absoluta'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # constrói URL absoluto
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':  # coleta URLs HTTP
                        self.links.add(absolute)

    def getLinks(self):
        'retorna URLs de hyperlink em seu formato absoluto'
        lista = list(self.links)
        return sorted(lista)

#Testanto a class Collector
url = 'https://caniuse.com/'
collectorParser = Collector(url)
html = getSource(url)
collectorParser.feed(html)
linksAbsolutos = collectorParser.getLinks()
for link in linksAbsolutos:
    print(link)

