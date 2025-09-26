año = int(input())

respuesta1 = "Es un año bisiesto"
respuesta2 = "No es un año bisiesto"

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print (respuesta1)
            
        else:
            print (respuesta2)
    else:
        print(respuesta1)
else:
    print(respuesta2)