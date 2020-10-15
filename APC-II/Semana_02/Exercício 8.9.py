'''Reimplemente o método dequeue() da classe Queue
 de modo que seja levantada uma exceção KeyboardInterrupt
  (um tipo de exceção impróprio, nesse caso) com a mensagem
   'remoção de uma fila vazia ' (uma mensagem de erro realmente apropriada)
    se for feita uma tentativa de remover algum elemento de uma fila vazia.
#>>> queue = Queue()
#>>> queue.dequeue()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    queue.dequeue()
  File "/Users/me/ch8.py", line 183, in dequeue
    raise KeyboardInterrupt('remoção de uma fila vazia')
KeyboardInterrupt: remoção de uma fila vazia'''

#Resolução

class Queue(list):
    'uma classe de fila, subclasse de list'

    def isEmpty(self):
        'retorna True se fila vazia, False caso contrário'
        return (len(self) == 0)

    def dequeue(self):
        'remove e retorna item na frente da fila'
        if self.isEmpty():
            raise KeyboardInterrupt('remoção de uma fila vazia ')
        return self.pop(0)

    def enqueue (self, item):
        'insere item no final da fila '
        return self.append(item)

# Teste
fila = Queue([1, 2])
print(fila)
fila.dequeue()
print(fila)
print('\n')

fila = Queue()
print(fila)
fila.dequeue()
print(fila)