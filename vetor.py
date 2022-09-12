class Vetor:

    def __init__(self, tamanho=5):
        self.items = []
        self.tamanho = tamanho
        self.cheios = 0

    def adicionar(self, item):
        if (self.cheios < self.tamanho):
            self.items.append(item)
            self.cheios+=1

    def __str__(self):
        return str(self.tamanho)

    def show(self):
        for i in range(self.tamanho):
            print(self.items[i])
