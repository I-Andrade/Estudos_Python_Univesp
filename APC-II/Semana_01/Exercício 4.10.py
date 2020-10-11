#Explique o que causa o erro de sintaxe em cada instrução listada anteriormente.
# Depois, escreva uma versão correta de cada instrução Python.

#>>> (3+4]
#SyntaxError: invalid syntax
# Resposta: A expressão deveria ser fechada com parênteses e não com chaves.
(3+4)

#>>> if x == 5
#SyntaxError: invalid syntax
# Resposta: O condicional deveria ter uma implementação depois do ':' (além do 'x' ter que ser definido antes).
x = 5
if x == 5:
    print('Esse é o número 5')

#>>> print 'hello'
#SyntaxError: invalid syntax
# Resposta: A função print exige que o parametro seja incluido dentro dos parenteses.
print('hello')

#>>> lst = [4;5;6]
#SyntaxError: invalid syntax
# Resposta: O separador de elementos da lista é ',' e não ';'.
lst = [4,5,6]

#>>> for i in range(10):
#print(i)
#SyntaxError: expected an indented block
# Resposta: O print(i) deve ser identado para pertencer ao for.
for i in range(10):
    print(i)
