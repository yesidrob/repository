def integral(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = coefficient / new_exponent
    
    # Formatear la salida como una cadena
    if new_coefficient.is_integer():
        new_coefficient = int(new_coefficient)
    
    if new_coefficient == 1:
        return f"x^{new_exponent}"
    else:
        return f"{new_coefficient}x^{new_exponent}"

# Solicitar al usuario que ingrese el coeficiente y el exponente
try:
    coefficient = int(input("Ingrese el coeficiente (número entero positivo): "))
    exponent = int(input("Ingrese el exponente (número entero positivo): "))
    
    if coefficient <= 0 or exponent < 0:
        print("Por favor, ingrese números enteros positivos.")
    else:
        result = integral(coefficient, exponent)
        print(f"La integral de {coefficient}x^{exponent} es: {result}")
except ValueError:
    print("Por favor, ingrese valores válidos.")