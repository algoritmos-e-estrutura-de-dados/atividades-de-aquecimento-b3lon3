import math

a = float(input("Numero A: "))
b = float(input("Numero B: "))
c = float(input("Numero C: "))

tri = ((a*c)/2)
cir = math.pi * (c*c)
tra = ((a+b)*c)/2
qua = b*b
ret = a*b

print(f" Triangulo: {tri}, \n Circulo: {cir}, \n Trapezio: {tra}, \n Quadrado: {qua}, \n Retanguo: {ret}")