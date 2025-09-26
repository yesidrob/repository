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
        reproduccion[artista].append(cancion)  # Agregamos la canción al final de la cola
        print(f"Reproduciendo {cancion} de {artista}.")

def listar_canciones(artista):
    # Listamos las canciones del artista
    if artista not in reproduccion or not reproduccion[artista]:
        print("El artista no tiene canciones registradas.")
    else:
        for i, cancion in enumerate(reproduccion[artista], start=1):
            print(f"{i}. {cancion}")

def procesar_comando(comando):
    # Procesamos el comando ingresado
    if comando == "añadir":
        print("ingrese cancion a añadir:")
        cancion = input()
        print("Ingrese el artista de la cancion a añadir:")
        artista = input()
        agregar_cancion(cancion, artista)
    elif comando == "reproducir":
        print("ingrese artista a reproducir:")
        artista = input()
        reproducir_cancion(artista)
    elif comando == "detener":
        print("Terminando la sesión. ¡Hasta pronto!")
        exit()
    elif comando == "listar":
        print("indique artista a listar:")
        artista = input()
        listar_canciones(artista)
    else:
        print("Comando no reconocido. Intente de nuevo:")

# Iniciamos el programa
while True:
    print("""indique que desea realizar: 
          añadir
          reproducir
          detener
          listar""")
    comando = input()
    procesar_comando(comando)