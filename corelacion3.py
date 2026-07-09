import pandas as pd

# Cargar archivo CSV
datos = pd.read_csv("estudiantes.csv")

# Correlación entre todas las variables numéricas
print("=== MATRIZ DE CORRELACIÓN ===")
correlaciones = datos[[
    "Matricula",
    "Asistencia",
    "Tareas",
    "Examen",
    "Calificacion_Final"
]].corr()

print(correlaciones)

# Correlación individual con Calificación Final
print("\n=== CORRELACIÓN CON CALIFICACIÓN FINAL ===")

corr_matricula = datos["Matricula"].corr(datos["Calificacion_Final"])
corr_asistencia = datos["Asistencia"].corr(datos["Calificacion_Final"])
corr_tareas = datos["Tareas"].corr(datos["Calificacion_Final"])
corr_examen = datos["Examen"].corr(datos["Calificacion_Final"])

print("Matrícula vs Calificación Final:", corr_matricula)
print("Asistencia vs Calificación Final:", corr_asistencia)
print("Tareas vs Calificación Final:", corr_tareas)
print("Examen vs Calificación Final:", corr_examen)