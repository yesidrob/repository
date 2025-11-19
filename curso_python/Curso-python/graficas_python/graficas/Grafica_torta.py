import pandas as pd
import matplotlib.pyplot as plt


datos= pd.read_excel('C:/Users/ADMIN/Desktop/workspace/datos local/Lista-de-clientes-con-nombre-y-direccion.xlsx',
            engine='openpyxl')

conteo= datos['Grupo de clientes'].value_counts()

plt.figure(figsize=(8, 8))
conteo.plot(kind='pie', autopct='%1.1f%%', startangle=90, legend=False,
    colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#CC99FF'],
    wedgeprops={'edgecolor': 'black'})

plt.title('Clientes por grupo')
plt.ylabel('')
plt.tight_layout()
plt.show()


