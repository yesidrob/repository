import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel
path = 'C:/Users/ADMIN/Desktop/workspace/datos local/Lista-de-clientes-con-nombre-y-direccion.xlsx'


datos = pd.read_excel(path, engine="openpyxl")
# Cargar los datos
"""try:
    datos = pd.read_excel(path, engine="openpyxl")
    print(datos.head())  # Ver las primeras filas para confirmar
except Exception as e:
    print(f"Error: {e}")"""

"""datos.to_string('output2.txt', index=False)  # Guardar el DataFrame en un archivo de texto
print("El archivo se ha cargado correctamente.")"""

conteo= datos['Grupo de clientes'].value_counts()
# Mostrar el conteo de cada grupo

plt.figure(figsize=(10, 6))
# Crear un gráfico de barras
conteo.plot(kind='bar', color='skyblue')
plt.title('Grupos de clientes')
plt.xlabel('Grupos')
plt.ylabel('Número de clientes')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
plt.tight_layout()
print("listo")
