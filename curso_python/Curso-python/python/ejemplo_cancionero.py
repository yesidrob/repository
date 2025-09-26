# Creamos un diccionario para almacenar las listas de reproducción por artista
reproduccion = {}

def agregar_cancion(cancion, artista):
    # Agregamos la canción a la lista de reproducción del artista
    if artista not in reproduccion:
        reproduccion[artista] = []
    reproduccion[artista].append(cancion)

def reproducir_cancion(artista):
    # Reproducimos la siguiente canción del artista
    if artista not in reproduccion or not reproduccion[artista]:
        if artista not in reproduccion:
            print("El artista no tiene canciones registradas.")
        else:
            print("No quedan canciones en cola.")
    else:
        cancion = reproduccion[artista].pop(0)
        print(f"Reproduciendo {cancion} de {artista}.")

def procesar_comando(comando):
    # Procesamos el comando ingresado
    if comando == "añadir":
        cancion = input()
        artista = input()
        agregar_cancion(cancion, artista)
    elif comando == "reproducir":
        artista = input()
        reproducir_cancion(artista)
    elif comando == "detener":
        print("Terminando la sesión. ¡Hasta pronto!")
        exit()
    else:
        print("Comando no reconocido. Intente de nuevo:")

# Iniciamos el programa
while True:
    comando = input()
    procesar_comando(comando)