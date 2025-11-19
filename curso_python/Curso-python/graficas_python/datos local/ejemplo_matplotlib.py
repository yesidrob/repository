import matplotlib.pyplot as plt

# Datos de ejemplo
ciudades = ['Lima', 'Cusco', 'Arequipa']
clientes = [50, 30, 20]

# Crear gráfica de barras
plt.bar(ciudades, clientes)
plt.title('Clientes por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Cantidad')
plt.show()
