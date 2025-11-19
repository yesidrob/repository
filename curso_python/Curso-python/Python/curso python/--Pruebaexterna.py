# Prueba del ejemplo de introduccion del curso unal.
x = 1
nombre = input("Por favor, ingrese su nombre: \n")
print(f"¡Hola {nombre}! \nLe damos la bienvenida al curso de Introduccion a la programacion con python")

total = 0
conjunto = set()
while(total< 5):
    fruta = input(f"Ingrese el nombre de una fruta, {5 - total} restantes.\n")
    conjunto.add(fruta)

    total = len(conjunto)

    print(f"Ha ingresado {total} {"fruta distinta"if total == 1 else "frutas distintas"}")

frutas = list(conjunto)
frutas.sort()
print("Estas son las frutas que ingreso alfabeticamente")

for fruta in [f"\t{i + 1}.\t {frutas[i]}" for i in range(len(frutas))]:
    print(fruta)

