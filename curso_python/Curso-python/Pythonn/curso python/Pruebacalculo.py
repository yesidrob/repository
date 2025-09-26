def switch ():
    global numero1, numero2
    numero1 = int(input("Introduzca el primer numero: ") )
    numero2 = int(input("Introduzca el segundo numero: ") )



while True:
    print("""
Indique la operacion a realizar: 
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Cambiar los numeros introducidos
    6) Salir de la calculadora
      """)
    
    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("RESULTADO: ",numero1," + ",numero2," = ",numero1+numero2)
    elif eleccion == 2:
        print(" ")
        print("RESULTADO: ",numero1," - ",numero2," = ",numero1-numero2)
    elif eleccion == 3:
        print(" ")
        print("RESULTADO: ",numero1," * ",numero2," = ",numero1*numero2)
    elif eleccion == 4:
        print(" ")
        print("RESULTADO: ",numero1," / ",numero2," = ",float(numero1/numero2))
    elif eleccion == 5:
        numero1 = int(input("Introduzca el primer numero: "))
        numero2 = int(input("Introduzca el segundo numero: "))
    elif eleccion == 6:
        print("Hasta pronto")