#Codigo que contenga listas de los nombres de los clientes junto con sus respectivos documentos de informacion
lista =["Maria", "Santiago", "Julian", "Andres", "Daniel", "Mateo", "David",  "Jose",  "Laura",  "Rosa", "Luis",  "Adolfo"]
print(lista)

print(lista[5])

#Eleccion en pantalla  
while True:
    print("""
Escoja el portafolio que desea abrir
          1)Maria
          2)Santiago
          3)Julian
          4)Andres
          5)Daniel
          6)Mateo
          7)David
          8)Jose
          9)Laura
          10)Rosa
          11)Luis
          12)Adolfo
          13)Salir
          """)
    eleccion= int(input())

    if eleccion == 1:
        print(lista[0])
    elif eleccion == 2:
        print(lista[1])
    elif eleccion == 3:
        print(lista[2])
    elif eleccion == 4:
        print(lista[3])
    elif eleccion == 5:
        print(lista[4])
    elif eleccion == 6:
        print(lista[5])
    elif eleccion == 7:
        print(lista[6])
    elif eleccion == 8:
        print(lista[7])
    elif eleccion == 9:
        print(lista[8])
    elif eleccion == 10:
        print(lista[9])
    elif eleccion == 11:
        print(lista[10])
    elif eleccion == 12:
        print(lista[11])
    
    elif eleccion == 13:
        print("Hasta pronto")
        break