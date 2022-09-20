import math

x1 = float(input("X1: "))
y1 = float(input("X2: "))
x2 = float(input("y1: "))
y2 = float(input("y2: "))


distancia = math.sqrt( ((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1)) )

print("Distancia: ", "{:.4f}".format(distancia) )


