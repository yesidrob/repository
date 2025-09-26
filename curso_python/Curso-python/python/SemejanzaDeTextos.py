#ingresan dos lineas de texto distintas
cadena = input().split()
conjunto_a = set(cadena)
cadena2 = input().split()
conjunto_b = set(cadena2)

#estas lineas de texto pertenecientes a los conjuntos a y b, se deben comparar para sacar semejantez.
interseccion = conjunto_a & conjunto_b 
#a y b se comparan para encontrar las palabras distintas.
diferencia_a_y_b = conjunto_a ^ conjunto_b
# ambos resultados se deben imprimir en cantidades, 1.palabras compartidas, 2.palabras unicas.

print(len(interseccion))
print(len(diferencia_a_y_b))
