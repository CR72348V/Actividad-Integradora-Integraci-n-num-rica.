import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calcular_integral():
    try:
        # Obtenemos los textos de la interfaz
        texto_f = entry_funcion.get()
        a = float(entry_a.get())
        b = float(entry_b.get())

        # Definimos la función de forma sencilla con eval
        def f(x):
            return eval(texto_f, {"x": x, "np": np, "sqrt": np.sqrt})

        # --- Cálculo de la integral sin librerías avanzadas (Regla del Trapecio básica) ---
        n = 1000  # Particiones
        dx = (b - a) / n
        suma = 0.5 * (f(a) + f(b))
        
        for i in range(1, n):
            xi = a + i * dx
            suma = suma + f(xi)
            
        area_total = suma * dx

        # Mostrar el resultado en el cuadro de texto
        txt_resultados.delete("1.0", tk.END)
        txt_resultados.insert(tk.END, "El valor de la integral es:\n")
        txt_resultados.insert(tk.END, f"{area_total:.8f}")

        # Dibujar la gráfica
        ax.clear()
        
        # 100 puntos en x, igual que en Scilab
        x = np.linspace(a, b, 100)
        y = f(x)
        
        # Graficamos la curva
        ax.plot(x, y, color="blue")
        
        # Dibujamos las líneas azules verticales una por una con un for simple
        for i in range(len(x)):
            ax.plot([x[i], x[i]], [0, y[i]], color="blue", linewidth=0.8)

        # Ajustes de los ejes para que empiece en 0
        ax.set_xlim(a, b)
        ax.set_ylim(bottom=0)
        
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", "Revisa la funcion o los numeros ingresados")

# --- Interfaz Tkinter ---
ventana = tk.Tk()
ventana.title("Integral definida")
ventana.geometry("900x500")
ventana.configure(bg="#fdfde0")

frame = tk.Frame(ventana, bg="#fdfde0")
frame.pack(side=tk.LEFT, padx=20)

# Entradas simples
tk.Label(frame, text="Ingrese la función:", bg="#fdfde0").pack()
entry_funcion = tk.Entry(frame, width=30)
entry_funcion.pack(pady=5)

tk.Label(frame, text="Límite inferior (a):", bg="#fdfde0").pack()
entry_a = tk.Entry(frame, width=15)
entry_a.pack(pady=5)

tk.Label(frame, text="Límite superior (b):", bg="#fdfde0").pack()
entry_b = tk.Entry(frame, width=15)
entry_b.pack(pady=5)
    

# Botón Calcular
tk.Button(frame, text="CALCULAR", bg="#98fb98", font=("Arial", 10, "bold"), command=calcular_integral).pack(pady=10)

# Texto de resultados
txt_resultados = tk.Text(frame, height=4, width=30, font=("Arial", 10))
txt_resultados.pack(pady=5)

# Gráfica a la derecha
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

ventana.mainloop()
