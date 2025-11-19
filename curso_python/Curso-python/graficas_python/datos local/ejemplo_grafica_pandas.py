import pandas as pd
import matplotlib.pyplot as plt

# Crear datos
datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo'],
    'Ventas': [100, 150, 120]
}

df = pd.DataFrame(datos)              # 1️⃣

df.set_index('Mes', inplace=True)     # 2️⃣

df.plot()                             # 3️⃣
plt.title("Ventas por Mes")           # 4️⃣
plt.ylabel("Ventas")                  # 5️⃣
plt.xlabel("Mes")                     # 6️⃣
plt.grid(True)                        # 7️⃣
plt.show()                            # 8️⃣
