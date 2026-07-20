import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos
df = pd.read_csv("estudiantes.csv")

# 2. Lista con las variables que quieres analizar (se ha quitado 'Edad')
variables = ["Matricula", "Asistencia", "Tareas", "Examen", "Horas_Estudio"]

# 3. Crear una figura con el número de filas y columnas adecuadas
# Si hay 5 variables, necesitamos 3 filas y 2 columnas para 6 espacios, con 1 sobrante.
# O se puede ajustar para tener 2 filas y 3 columnas para 6 espacios.
# Ajustamos para 2 filas y 3 columnas para mejor visualización.
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

# 4. Aplanar la matriz de ejes para recorrerla fácilmente
axes = axes.flatten()

# 5. Dibujar cada gráfica de dispersión
for i, var in enumerate(variables):
    axes[i].scatter(df[var], df["Calificacion_Final"], color="royalblue", alpha=0.7)
    axes[i].set_xlabel(var)
    axes[i].set_ylabel("Calificación Final")
    axes[i].set_title(f"{var} vs Calificación Final")
    axes[i].grid(True, linestyle="--", alpha=0.5)

# 6. Ocultar los gráficos sobrantes (en este caso, el último si hay 5 variables y 6 espacios)
for j in range(len(variables), len(axes)):
    axes[j].axis('off')

# 7. Ajustar diseño y mostrar
plt.tight_layout()
plt.show()