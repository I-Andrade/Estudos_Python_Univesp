from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

'''Aumente a classe Collector de modo que ela também colete todos os dados de texto em uma string que
 pode ser recuperada usando o método getData().

>>> url = 'http://www.w3.org/Consortium/mission.html'
>>> resource = urlopen(url)
>>> content = resource.read().decode()
>>> collector = LinksCollector(url)
>>> collector.feed(content)
>>> collector.getData()

'\nW3C Mission\n ...'

(Somente os primeiros caracteres são apresentados.)'''

def getSource(url):
    'returns the content of resource specified by url as a string'
    response = urlopen(url)
    html = response.read()
    return html.decode()

#HTMLParser com metodos personalizados através de herança
class Collector(HTMLParser):
    'coleta URLs de hyperklink em uma lista'

    def __init__(self, url):
        'inicializa analisador, o URL e uma lista'
        HTMLParser.__init__(self)
        self.url = url
        self.links = set()
        #self.data = list()
        self.text = ''

    def handle_starttag(self, tag, attrs):
        'coleta URLs de hyperlink em sua forma absoluta'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # constrói URL absoluto
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':  # coleta URLs HTTP
                        self.links.add(absolute)

    #Versão inicial
    #def handle_data(self, data):
    #  data = str.strip(data)
    #  self.data.append(data)

    #Versão corrigida
    def handle_data(self, data):
        'coleta e concatena dados de texto'
        self.text += data

    def getLinks(self):
        'retorna URLs de hyperlink em seu formato absoluto'
        lista = list(self.links)
        return sorted(lista)

    def getData(self):
        return self.text
        #return self.data (Versão inicial)

#Testanto a class Collector
url = 'https://caniuse.com/'
collectorParser = Collector(url)
html = getSource(url)
collectorParser.feed(html)
linksAbsolutos = collectorParser.getLinks()
dadosobtidos = collectorParser.getData()
for link in linksAbsolutos:
    print(link)
#for dados in dadosobtidos:    (Versão inicial)
#    print(dados)
print()
print(dadosobtidos)