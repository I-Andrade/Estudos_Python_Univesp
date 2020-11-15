from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
class Crawler2():


    def __init__(self):
        self.paginasVisitadas = set()

    def getSource(self, urlParaDecodificar):
        'returns the content of resource specified by url as a string'
        response = urlopen(urlParaDecodificar)
        html = response.read()
        return html.decode()

    def paginaVisitada(self, urlVisitado):
        self.paginasVisitadas.add(urlVisitado)
        return print('Visitando {}'.format(urlVisitado))

    def analyse(self, url):
        urlDecodificado = self.getSource(url)
        coletorDeLinks = Collector(url)
        coletorDeLinks.feed(urlDecodificado)
        links = coletorDeLinks.getLinks()
        self.paginaVisitada(url)
        for link in links:
            if link not in self.paginasVisitadas:
                try:
                    self.analyse(link)
                except:
                    pass

class Collector(HTMLParser):
    'coleta URLs de hyperklink em um conjunto'

    def __init__(self, url):
        'inicializa analisador, o URL e um conjunto'
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
        return lista



#Testando
objetoCrawler = Crawler2()
objetoCrawler.analyse('http://reed.cs.depaul.edu/lperkovic/one.html')