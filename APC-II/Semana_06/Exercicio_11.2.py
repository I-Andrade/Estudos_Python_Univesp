from html.parser import HTMLParser
from urllib.request import urlopen

'''Desenvolva a classe MyHTMLParser como uma subclasse de HTMLParser que, quando alimentada com um arquivo HTML, mostra os nomes das tags de início e fim na ordem em que aparecem no documento, e com um recuo proporcional à profundidade do elemento na estrutura de árvore do documento. Ignore os elementos HTML que não exigem uma tag de fim, como p e br.
Arquivo: w3c.html
>>> infile = open('w3c.html')
>>> content = infile.read()
>>> infile.close()
>>> myparser = MyHTMLParser()
>>> myparser.feed(content)
html start
    head start
        title start
        title end
    head end
    body start
        h1 start
        h1 end
        h2 start
        h2 end
        ul start
            li start
...
        a end
    body end
html end'''

def getSource(url):
    'returns the content of resource specified by url as a string'
    response = urlopen(url)
    html = response.read()
    return html.decode()

conteudo = getSource('https://www.contabilizei.com.br/')
#infile = open('google.html')
#conteudo = infile.read()
#infile.close()

#HTMLParser com metodos personalizados através de herança
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.contador = 0
        self.tagsexcluidas = ['br', 'p', 'meta', 'link', 'script', 'source', 'img', 'hr', 'input']

    def handle_starttag(self, tag, attrs):
        if tag not in self.tagsexcluidas:
            print("{}{} start".format(self.contador*" ", tag))
            self.contador +=2

    def handle_endtag(self, tag):

        if tag not in self.tagsexcluidas:
            self.contador -= 2
            print("{}{} end".format(self.contador*" ", tag))


myparser = MyHTMLParser()
myparser.feed(conteudo)