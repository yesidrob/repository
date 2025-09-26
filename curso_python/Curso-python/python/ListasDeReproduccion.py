#gustos similares en artistas preferidos
#diferencias en elegir una cancion de un artista
lista = {}
#Añadir : dos lineas, 1.nombre de la cancion, 2.nombre del artista, y se agregan a una lista de reproduccion.
def añadir (): 
    cancion = input()
    artista = input()
    if artista in lista:
        lista[artista] = cancion

#Reproducir : ingresa el nombre de un artista, imprimir la siguiente cancion a reproducirse.
def reproducir ():
    artista_escuchar = input()
    if artista_escuchar in lista:
        if cancion[artista]:
           print(f"Reproduciendo {cancion[artista].pop(0)} de {artista}.")
        else: 
            print("No quedan canciones en cola")
    else:
        print("El artista no tiene canciones registradas.")
    

#Las canciones se reproduciran en el orden en que fueron añadidas, primero las cancones mas antiguas y eliminando las canciones conforme se van reproduciendo.
#Si el artista tiene canciones en cola __ Reproduciendo <cancion> de <artista>. 
#Si ya se reprodujeron todas las canciones__No quedan canciones en cola.
#si el artista ingresado no tiene canciones registradas___El artista no tiene canciones registradas.
#Detener : Terminando la sesion. ¡Hasta pronto! 
def detener ():
    print("Terminando la sesión. ¡Hasta pronto!")
    

#Si el comando ingresado esta mal escrito ____Comando no reconocido. Intente de nuevo
while True :
   comando = input().lower()

    if  comando == "añadir":
       