#MEDIDAS DE TENDENCIA
import pandas as pd

df = pd.read_csv('/content/estudiantes.csv')

variables = ['Asistencia', 'Tareas', 'Examen']

resultados = []

for var in variables:
    media = df[var].mean()
    mediana = df[var].median()
    moda = df[var].mode().iloc[0]

    resultados.append([
        var,
        round(media, 2),
        mediana,
        moda
    ])

tabla = pd.DataFrame(
    resultados,
    columns=['Variable', 'Media', 'Mediana', 'Moda']
)

print("Tabla de Medidas de Tendencia Central")
print(tabla)

mayor_promedio = tabla.loc[tabla['Media'].idxmax()]

print("\nVariable con el promedio más alto:")
print(f"{mayor_promedio['Variable']} ({mayor_promedio['Media']})")

print("\nComparación Media y Mediana:")
for i, fila in tabla.iterrows():
    diferencia = abs(fila['Media'] - fila['Mediana'])
    if diferencia < 3:
        print(f"{fila['Variable']}: Sí son parecidas.")
    else:
        print(f"{fila['Variable']}: No son muy parecidas.")

        #interpretacion:
        #asistenacia: el promedio de asistencia es de 82.05%
        #tareas: el promedio de tareas es de 83.25%
        #Examen: el promedio del examen es de 80.35 reflejando un rendimiento aceptable