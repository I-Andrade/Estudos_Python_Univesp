from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
from re import findall
class Crawler2():


    def __init__(self):
        self.paginasVisitadas = set()

    def frequencyRE(self, string):
        dicionario = dict()
        listaComPalavras = findall('[a-zA-Z]+', string)

        for palavra in listaComPalavras:
            if palavra in dicionario:
                dicionario[palavra] += 1
            else:
                dicionario[palavra] = 1

        return dicionario

    def getSource(self, urlParaDecodificar):
        'returns the content of resource specified by url as a string'
        response = urlopen(urlParaDecodificar)
        html = response.read()
        return html.decode()

    def paginaVisitada(self, urlVisitado):
        self.paginasVisitadas.add(urlVisitado)
        print()
        print('___________________________________________________________________________________________')
        return print('Visitando {}'.format(urlVisitado))

    def analyse(self, url):
        urlDecodificado = self.getSource(url)
        coletor = Collector(url)
        coletor.feed(urlDecodificado)
        links = coletor.getLinks()
        dados = coletor.getData()
        frequenciaPalavras = self.frequencyRE(dados)
        self.paginaVisitada(url)

        # mostra frequência de cada palavra na página Web
        print('\n{:50} {:10} {:5}'.format('URL', 'PALAVRAS', 'QUANTIDADE '))
        for word in frequenciaPalavras:
            print('{:50} {:10} {:5}'.format(url, word, frequenciaPalavras[word]))

        # mostra links http encontrados na página Web
        print('\n{:50} {:10}'.format('URL', 'LINK'))
        for link in links:
            print('{:50} {:10}'.format(url, link))
        print('___________________________________________________________________________________________')

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
        self.text = ''

    def handle_data(self, data):
        'coleta e concatena dados de texto'
        self.text += data

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


    def getData(self):
        return self.text

#Testando
objetoCrawler = Crawler2()
objetoCrawler.analyse('http://reed.cs.depaul.edu/lperkovic/one.html')