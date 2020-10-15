#Comece definindo a classe Teste e depois criando duas instâncias de Teste
# no seu shell do interpretador:
#>>>
#class Teste:
#    versão = 1.02
#>>> a = Teste()
#>>> b = Teste()


class Teste:
    versao = 1.02

a = Teste()
b = Teste()
#A classe Teste tem apenas um atributo, a variável de classe versão, que se refere ao valor float 1.02.
# (a)Desenhe os namespaces associados à classe e aos dois objetos, os nomes – se houver – neles contidos
# e os valores aos quais os nomes se referem.
# Resolução
# namespaces da classe: versao (aponta para objeto 1.02)
# namespaces do objeto a: vazio
# namespaces da objeto b: vazio
# (b)Execute essas instruções e preencha os pontos de interrogação:
    # >>> a.versao ??? = 1.02
    # >>> b.versao ??? = 1.02
    # >>> Teste.versao ??? = 1.02
    # >>> Teste.versao=1.03
    # >>> a.versao ??? = 1.03
    # >>> Teste.versao ??? = 1. 03
    # >>> a.versao = 'Última!!'
    # >>> Teste.versao ??? = 1.03
    # >>> b.versao ??? = 1.03
    # >>> a.versao ??? = 'Última!!'

# (c)Desenhe o estado dos namespaces após essa execução.
# namespaces da classe: versao (aponta para objeto 1.03)
# namespaces do objeto a: versao (aponta para objeto 'Última!!')
# namespaces da objeto b: vazio
    # Explique por que as três últimas expressões são avaliadas dessa forma.
    # Resolução: Ao atribuir a.versao, é criado no namespace de a a variavel versao.
