#juego de texto

numero_secreto = int(input())
intentos = int(input())
minimo = int(input())
maximo = int(input())
print(f"¡Bienvenido! Por favor ingrese números entre {minimo} y {maximo} para ganar.")

while True:
#identificar si se acabaron los intentos.
 if 0 == intentos:
  print(f"Se acabaron los intentos. El número correcto era {numero_secreto}.")
  break
 
 print(f"Intentos restantes: {intentos}.")
 x = int(input())

 #identificar si x esta en el rango de numeros.
 if minimo<=x<=maximo:
  intentos = intentos - 1
  if x == numero_secreto:
   print("¡Felicidades! El número ingresado es correcto.")
   break
  #identificar si se acabaron los intentos.
  elif 0 == intentos:
   print(f"Se acabaron los intentos. El número correcto era {numero_secreto}.")
   break
 #identificar si x es mayor que el numero correcto.
  elif x > numero_secreto:
    print("Respuesta incorrecta. El número que ingresó es mayor que el número secreto.")
 #identificar si x es menor que el numero correcto.
  elif x < numero_secreto:
    print("Respuesta incorrecta. El número que ingresó es menor que el número secreto.")
 else:
  print("El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente")
 

print("Fin del juego. ¡Gracias por participar!")