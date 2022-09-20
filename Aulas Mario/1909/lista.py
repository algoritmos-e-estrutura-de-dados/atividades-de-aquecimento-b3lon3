from node import Node


class Lista:
    inicio = None

    def __init__(self):
        self.inicio = None

    def adicionar(self, valor, inicio=True):
        if inicio:
            self.adicionar_no_inicio(valor)
        else:
            self.adicionar_no_fim(valor)

    def remover(self, valor):
        anterior = None
        aux = self.inicio

        while (aux != valor):
            anterior = aux
            aux = aux.proximo
        self.valor = None



    def adicionar_no_inicio(self, valor):
        print("nao fiz kkk")

    def adicionar_no_fim(self, valor):
        if (self.inicio == None):
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio
            while (aux.proximo != None):
                aux = aux.proximo
            aux.proximo = Node(valor, None)

    def show(self):
        aux = self.inicio
        print("[", end='')
        while (aux.proximo != None):
            print(aux.valor, end=', ')
            aux = aux.proximo
        print(aux.valor)
        print("]")
