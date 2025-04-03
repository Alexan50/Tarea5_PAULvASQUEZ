#calculo de la media y mediana de edades añadir la varianza y  desviacion estandar 

import numpy as np
import matplotlib.pyplot as plt 

edades = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

plt.axvline(np.mean(edades), color='r', linestyle='--', label=f"media: {np.mean(edades):.1f}")
plt.axvline(np.median(edades), color='g', linestyle='-.', label=f"mediana: {np.median(edades):.1f}")

plt.title(f"var: {np.var(edades):.2f} | Desv: {np.std(edades):.2f}")
plt.legend()
plt.show()
