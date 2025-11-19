

#debemos asegurarnos que el numero de votos quede registrado en una variable.
#lo que ingrese al sistema se debe organizar en un diccionario, candidato : votos.
#debemos contar los votos de cada uno de los candidatos.
#debemos comparar el valor de los votos de cada candidato con los demas candidatos para hallar un ganador o un empate.

n = int(input())

diccionario = {}
for i in range(n):
    candidato = input()
    
    if candidato in diccionario: 
        diccionario[candidato] += 1
    else:
        diccionario[candidato] = 1

max_votos = max(diccionario.values())
ganador = [candidato for candidato, votos in diccionario.items() if votos == max_votos]

if len(ganador) > 1:
    print("EMPATE")
else:
    print(ganador[0])

    #correccion 
    #debo pensar paso a paso, debido a que mientras van ingresando los datos asi mismo se van contando, es decir, cuando se mencionan los nombres de los candidatos o se ingresan es pq alguien los a votado,
    #asique debemos registrar el nombre del candidato e inmediatamente 1 voto, asi a medida que identifique que el nombre ya halla sido ingresado en el sistema solo sumemos 1 voto en cada momento,
    #tambien cabe aclarar que para crear un diccionario debemos crearlo vacio para luego ingresar los nombres de cada candidato ingresado en el sistema, por consiguiente, lo pasamos primero por el filtro que 
    # vigila si el candidato ingresado a sido registrado anteriormente para asi solo sumar un voto mas a ese candidato y no crear una clave doble.
    #luego escribimos una funcion que identifique cual valor de votos es el mayor, en este caso el mayor valor de todos es 2
    #instruimos un cadigo que mire candidato por candidato cual cumple con los requerimientos es decir, clave : valor = clave : 2, y lo guardamos en una lista.
    #finalmente hacemos una condicion que mire si en la lista hay mas de un objeto o candidato = EMPATE, de lo contrario hay un ganador, ya que al encontrarse un solo candidato en la lista este seria el ganador oficialmente.