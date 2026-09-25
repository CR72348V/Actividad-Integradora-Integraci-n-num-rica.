import numpy as np
import matplotlib.pyplot as plt 

title = input("Ingrese el título de la gráfica: ")
funcion = input("Ingrese la función a graficar (en términos de x): ")
limit = float(input("Ingrese el límite inferior para la gráfica: "))
limit = float(input("Ingrese el límite superior para la gráfica: "))

x = np.arange(limin, limite, 0.1)
y = np.array([eval(funcion), {"x":val,"np":np} for val in x])

plt.plot(x, y, color= "red", linewidth= 3)
plt.grid(True, linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title(title)
plt.show()

        