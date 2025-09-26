def introducirNumeros ():
    global numero1, numero2
    numero1 = int(input("Introduzca el primer numero: "))
    numero2 = int(input("Introduzca el segundo numero: "))

def sumar ( a, b):
    print("La suma de ",a," + ",b," = ",a+b)

def restar (a, b): 
    print("La resta de ",a," - ",b," = ",a-b)

def multiplicacion (a, b):
    print("La multiplicacion de ",a," * ",b," = ",a*b)

def division (a, b):
    if b == 0:
        print("No se puede dividir entre cero")
    else:
        print("La division de ",a," / ",b," = ",a/b)

while True:
    print("""Indique la operacion a realizar:
          1) Sumar
          2) Restar
          3) Multiplicar
          4) Dividir
          5) Salir de la calculadora
          """)
    eleccion = int(input())

    if 1>eleccion>5:
        print("El numero ingresado no corresponde")

    elif eleccion == 1:
        introducirNumeros()
        sumar ( numero1, numero2)
    elif eleccion == 2:
        introducirNumeros()
        restar( numero1, numero2)
    elif eleccion == 3:
        introducirNumeros()
        multiplicacion(numero1, numero2)
    elif eleccion == 4:
        introducirNumeros()
        division(numero1, numero2)
    elif eleccion == 5:
        print("Hasta pronto")
        break