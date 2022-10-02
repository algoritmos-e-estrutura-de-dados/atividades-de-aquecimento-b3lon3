a = input("Codigo, Numero e Valor de peça 1:")
b = input("Codigo, Numero e Valor de peça 2:")

p1 = a.split()
p2 = b.split()

c1, n1, v1 = p1[0], p1[1], p1[2]
c2, n2, v2 = p2[0], p2[1], p2[2]

preco = (int(n1) * float(v1) + int(n2) * float(v2))

print(f"Preço a ser pago:", preco)
