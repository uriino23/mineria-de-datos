import pandas as pd

# Cargar archivo CSV
df = pd.read_csv('/content/estudiantes.csv')

# Variables a analizar (se ha quitado 'Edad' y añadido 'Horas_Estudio')
variables = [
    'Matricula',
    'Asistencia',
    'Tareas',
    'Examen',
    'Calificacion_Final',
    'Horas_Estudio'
]

resultados = []

for var in variables:
    rango = df[var].max() - df[var].min()
    varianza = df[var].var()
    desviacion = df[var].std()

    resultados.append([
        var,
        round(rango, 2),
        round(varianza, 2),
        round(desviacion, 2)
    ])

tabla = pd.DataFrame(
    resultados,
    columns=[
        'Variable',
        'Rango',
        'Varianza',
        'Desviación Estándar'
    ]
)

print("MEDIDAS DE DISPERSIÓN")
print(tabla)