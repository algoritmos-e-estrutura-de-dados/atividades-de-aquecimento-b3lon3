from node import Node

class Lista:
    inicio = None

    def __init__(self):
        self.inicio = None

    #add end of the list
    def adicionar(self, valor):
        if(self.inicio == None):
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio
            while (aux.proximo != None):
                aux = aux.proximo

            aux.proximo = Node(valor, None)

    def show(self):
        aux = self.inicio
        print("[", end = '')
        while (aux.proximo != None):
            print(f'{aux.valor}', end = ', ')
            aux = aux.proximo
        print(aux.valor)
        print("]")
