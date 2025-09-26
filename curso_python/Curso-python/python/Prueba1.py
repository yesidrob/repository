###Given an integral number, determine if it's a square number:
#In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
#The tests will always use some integral number, so don't worry about that in dynamic typed languages.

import math

def es_producto_cuadrado(n):
    if n < 0:
        return False
    raiz = math.sqrt(n)
    return raiz == int(raiz)

n = int(input("Ingrese un número entero: "))
if es_producto_cuadrado(n):
    print(f"{n} es producto de un cuadrado perfecto")
else:
    print(f"{n} no es producto de un cuadrado perfecto")


    import math

def es_producto_cuadrado(n):
    return math.sqrt(n) == int(math.sqrt(n))

n = int(input("Ingrese un número entero: "))
print(es_producto_cuadrado(n))


#sin extension o importacion:
def es_producto_cuadrado(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

n = int(input("Ingrese un número entero: "))
print(es_producto_cuadrado(n))