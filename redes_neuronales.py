
# EJERCICIO DE REDES NEURONALES
# Archivo: equipos_computo.csv

# 1. IMPORTAR LIBRERÍAS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import warnings
warnings.filterwarnings("ignore")


# 2. SUBIR EL ARCHIVO CSV MANUALMENTE


print("Selecciona el archivo equipos_computo.csv")

uploaded = files.upload()

nombre_archivo = list(uploaded.keys())[0]

print("\nArchivo cargado correctamente:", nombre_archivo)


# 3. CARGAR EL ARCHIVO

df = pd.read_csv(nombre_archivo)

print("\n==============================")
print("PRIMEROS 5 REGISTROS")
print("==============================")

display(df.head())

# 4. INFORMACIÓN GENERAL DEL DATASET

print("\n==============================")
print("DIMENSIONES DEL DATASET")
print("==============================")

print("Número de filas:", df.shape[0])
print("Número de columnas:", df.shape[1])


print("\n==============================")
print("COLUMNAS")
print("==============================")

print(df.columns.tolist())


print("\n==============================")
print("TIPOS DE DATOS")
print("==============================")

print(df.dtypes)

# 5. REVISAR VALORES NULOS

print("\n==============================")
print("VALORES NULOS")
print("==============================")

print(df.isnull().sum())

# 6. REVISAR REGISTROS DUPLICADOS

duplicados = df.duplicated().sum()

print("\n==============================")
print("REGISTROS DUPLICADOS")
print("==============================")

print("Cantidad de registros duplicados:", duplicados)

# 7. LIMPIEZA DE DATOS

# Eliminar duplicados si existen
df = df.drop_duplicates()

# Eliminar filas que tengan valores nulos
df = df.dropna()

print("\nDatos después de la limpieza:")
print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])

# 8. ESTADÍSTICAS DESCRIPTIVAS

print("\n==============================")
print("ESTADÍSTICAS DESCRIPTIVAS")
print("==============================")

display(df.describe())

# 9. DISTRIBUCIÓN DEL ESTADO DE LOS EQUIPOS

print("\n==============================")
print("DISTRIBUCIÓN DE ESTADO_EQUIPO")
print("==============================")

print(df["Estado_Equipo"].value_counts())


plt.figure(figsize=(8,5))

df["Estado_Equipo"].value_counts().plot(kind="bar")

plt.title("Distribución del estado de los equipos")
plt.xlabel("Estado del equipo")
plt.ylabel("Cantidad de equipos")

plt.xticks(rotation=0)

plt.show()

# 10. DISTRIBUCIÓN POR LABORATORIO

plt.figure(figsize=(9,5))

df["Laboratorio"].value_counts().plot(kind="bar")

plt.title("Cantidad de equipos por laboratorio")
plt.xlabel("Laboratorio")
plt.ylabel("Cantidad")

plt.xticks(rotation=45)

plt.show()

# 11. TEMPERATURA DE CPU SEGÚN ESTADO

estados = df["Estado_Equipo"].unique()

datos_temperatura = [
    df[df["Estado_Equipo"] == estado]["Temperatura_CPU"]
    for estado in estados
]

plt.figure(figsize=(8,5))

plt.boxplot(datos_temperatura, labels=estados)

plt.title("Temperatura de CPU según estado del equipo")
plt.xlabel("Estado")
plt.ylabel("Temperatura CPU")

plt.show()

# 12. TIEMPO DE ARRANQUE SEGÚN ESTADO

datos_arranque = [
    df[df["Estado_Equipo"] == estado]["Tiempo_Arranque_Segundos"]
    for estado in estados
]

plt.figure(figsize=(8,5))

plt.boxplot(datos_arranque, labels=estados)

plt.title("Tiempo de arranque según estado")
plt.xlabel("Estado del equipo")
plt.ylabel("Tiempo de arranque en segundos")

plt.show()

# 13. DEFINIR VARIABLES X y Y

# ID_Equipo no se utiliza para entrenar porque solamente
# identifica a cada computadora y no representa una característica
# útil para determinar el estado.

X = df.drop(columns=["ID_Equipo", "Estado_Equipo"])

y = df["Estado_Equipo"]


print("\n==============================")
print("VARIABLES UTILIZADAS")
print("==============================")

print("\nVariables de entrada:")
print(X.columns.tolist())

print("\nVariable objetivo:")
print("Estado_Equipo")

# 14. IDENTIFICAR VARIABLES NUMÉRICAS Y CATEGÓRICAS

columnas_numericas = [
    "Horas_Uso_Semanal",
    "Temperatura_CPU",
    "Uso_RAM_Porcentaje",
    "Espacio_Disco_Libre",
    "Errores_Sistema",
    "Tiempo_Arranque_Segundos"
]

columnas_categoricas = [
    "Laboratorio"
]


# 15. PREPROCESAMIENTO

# Variables numéricas:
# Se normalizan utilizando StandardScaler.
#
# Variables categóricas:
# Se convierten a números mediante OneHotEncoder.

preprocesador = ColumnTransformer(
    transformers=[
        (
            "numericas",
            StandardScaler(),
            columnas_numericas
        ),

        (
            "categoricas",
            OneHotEncoder(handle_unknown="ignore"),
            columnas_categoricas
        )
    ]
)


# 16. CREAR LA RED NEURONAL

red_neuronal = MLPClassifier(

    # Dos capas ocultas:
    # Primera capa = 16 neuronas
    # Segunda capa = 8 neuronas
    hidden_layer_sizes=(16, 8),

    activation="relu",

    solver="adam",

    max_iter=2000,

    random_state=42
)


# 17. CREAR PIPELINE

modelo = Pipeline(
    steps=[
        ("preprocesamiento", preprocesador),
        ("red_neuronal", red_neuronal)
    ]
)


# 18. DIVIDIR DATOS EN ENTRENAMIENTO Y PRUEBA


X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


print("\n==============================")
print("DIVISIÓN DE LOS DATOS")
print("==============================")

print("Datos de entrenamiento:", len(X_train))
print("Datos de prueba:", len(X_test))


# 19. ENTRENAR LA RED NEURONAL

print("\nEntrenando la red neuronal...")

modelo.fit(X_train, y_train)

print("Entrenamiento terminado correctamente.")


# 20. REALIZAR PREDICCIONES

y_pred = modelo.predict(X_test)


# 21. CALCULAR EXACTITUD

exactitud = accuracy_score(y_test, y_pred)

print("\n==============================")
print("EXACTITUD DEL MODELO")
print("==============================")

print(f"Exactitud: {exactitud:.4f}")

print(f"Porcentaje de aciertos: {exactitud * 100:.2f}%")


# 22. REPORTE DE CLASIFICACIÓN

print("\n==============================")
print("REPORTE DE CLASIFICACIÓN")
print("==============================")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)

# 23. MATRIZ DE CONFUSIÓN

print("\n==============================")
print("MATRIZ DE CONFUSIÓN")
print("==============================")

matriz = confusion_matrix(
    y_test,
    y_pred,
    labels=modelo.classes_
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=matriz,
    display_labels=modelo.classes_
)

disp.plot()

plt.title("Matriz de confusión - Red neuronal")

plt.show()

# 24. COMPARAR RESULTADOS REALES Y PREDICCIONES

resultados = pd.DataFrame({

    "Estado_Real": y_test.values,

    "Estado_Predicho": y_pred

})

resultados["Prediccion_Correcta"] = (
    resultados["Estado_Real"] ==
    resultados["Estado_Predicho"]
)


print("\n==============================")
print("COMPARACIÓN DE RESULTADOS")
print("==============================")

display(resultados)

# 25. VALIDACIÓN CRUZADA

print("\n==============================")
print("VALIDACIÓN CRUZADA")
print("==============================")

# Utilizamos 5 divisiones
cv = StratifiedKFold(

    n_splits=5,

    shuffle=True,

    random_state=42
)


scores = cross_val_score(

    modelo,

    X,

    y,

    cv=cv,

    scoring="accuracy"
)


print("Exactitud obtenida en cada prueba:")

for i, score in enumerate(scores, start=1):

    print(
        f"Prueba {i}: "
        f"{score:.4f} "
        f"({score * 100:.2f}%)"
    )


print(
    "\nExactitud promedio:"
)

print(
    f"{scores.mean():.4f} "
    f"({scores.mean()*100:.2f}%)"
)


print(
    "\nDesviación estándar:"
)

print(
    f"{scores.std():.4f}"
)

# 26. GRÁFICA DE VALIDACIÓN CRUZADA

plt.figure(figsize=(8,5))

plt.bar(
    range(1, len(scores)+1),
    scores * 100
)

plt.axhline(
    scores.mean()*100,
    linestyle="--",
    label="Promedio"
)

plt.xlabel("Prueba")

plt.ylabel("Exactitud (%)")

plt.title(
    "Resultados de validación cruzada"
)

plt.ylim(0,105)

plt.legend()

plt.show()

# 27. CURVA DE PÉRDIDA DURANTE EL ENTRENAMIENTO

mlp_entrenado = modelo.named_steps["red_neuronal"]

plt.figure(figsize=(8,5))

plt.plot(
    mlp_entrenado.loss_curve_
)

plt.title(
    "Curva de pérdida de la red neuronal"
)

plt.xlabel(
    "Iteraciones"
)

plt.ylabel(
    "Pérdida"
)

plt.show()

# 28. EJEMPLO DE NUEVA PREDICCIÓN

nuevo_equipo = pd.DataFrame({

    "Laboratorio": [
        "Lab_A"
    ],

    "Horas_Uso_Semanal": [
        40
    ],

    "Temperatura_CPU": [
        70
    ],

    "Uso_RAM_Porcentaje": [
        75
    ],

    "Espacio_Disco_Libre": [
        150
    ],

    "Errores_Sistema": [
        3
    ],

    "Tiempo_Arranque_Segundos": [
        60
    ]

})


print("\n==============================")
print("DATOS DEL NUEVO EQUIPO")
print("==============================")

display(nuevo_equipo)


prediccion_nueva = modelo.predict(
    nuevo_equipo
)


print(
    "\nEstado predicho para "
    "el nuevo equipo:"
)

print(
    prediccion_nueva[0]
)

# 29. PROBABILIDADES DE LA PREDICCIÓN

probabilidades = modelo.predict_proba(
    nuevo_equipo
)[0]


tabla_probabilidades = pd.DataFrame({

    "Estado":
        modelo.classes_,

    "Probabilidad":
        probabilidades

})


tabla_probabilidades[
    "Porcentaje"
] = (

    tabla_probabilidades[
        "Probabilidad"
    ] * 100

).round(2)


print("\n==============================")
print("PROBABILIDAD DE CADA ESTADO")
print("==============================")

display(
    tabla_probabilidades
)

# 30. INTERPRETACIÓN AUTOMÁTICA

print("\n")
print("=" * 70)

print(
    "INTERPRETACIÓN DE RESULTADOS"
)

print("=" * 70)


print(
    "\n1. Se utilizó una red neuronal "
    "artificial del tipo MLPClassifier."
)


print(
    "\n2. La variable que se intentó "
    "predecir fue Estado_Equipo."
)


print(
    "\n3. Los posibles estados son:"
)

for clase in modelo.classes_:

    print("-", clase)


print(
    f"\n4. La exactitud obtenida "
    f"con el conjunto de prueba fue "
    f"de {exactitud*100:.2f}%."
)


print(
    f"\n5. La exactitud promedio "
    f"utilizando validación cruzada "
    f"fue de {scores.mean()*100:.2f}%."
)


print(
    "\n6. La matriz de confusión permite "
    "observar cuántos equipos fueron "
    "clasificados correctamente y "
    "cuáles fueron confundidos."
)


print(
    "\n7. La validación cruzada permite "
    "comprobar si el rendimiento del "
    "modelo se mantiene al utilizar "
    "diferentes grupos de entrenamiento "
    "y prueba."
)


if scores.mean() >= 0.90:

    print(
        "\nCONCLUSIÓN: El modelo presenta "
        "una fiabilidad MUY ALTA."
    )

elif scores.mean() >= 0.80:

    print(
        "\nCONCLUSIÓN: El modelo presenta "
        "una fiabilidad ALTA."
    )

elif scores.mean() >= 0.70:

    print(
        "\nCONCLUSIÓN: El modelo presenta "
        "una fiabilidad ACEPTABLE."
    )

else:

    print(
        "\nCONCLUSIÓN: El modelo presenta "
        "una fiabilidad BAJA y sería "
        "necesario mejorar el entrenamiento."
    )


print("\n")
print("=" * 70)

print("ANÁLISIS FINAL")

print("=" * 70)


print(
    """
La red neuronal fue entrenada utilizando información
relacionada con el uso y funcionamiento de los equipos
de cómputo, incluyendo las horas de uso semanal,
temperatura del CPU, porcentaje de memoria RAM utilizada,
espacio libre en disco, cantidad de errores del sistema
y tiempo de arranque.

La variable objetivo fue Estado_Equipo, permitiendo
clasificar las computadoras en diferentes niveles de
funcionamiento.

Para evaluar la fiabilidad del modelo se utilizó un
conjunto independiente de prueba y posteriormente se
aplicó validación cruzada de cinco particiones.

Una exactitud alta indica que las características
registradas permiten identificar adecuadamente el
estado de los equipos.

La matriz de confusión permite identificar los casos
correctamente clasificados y los posibles errores entre
las categorías.

Este tipo de modelo puede ser útil dentro de una
institución para detectar computadoras que necesitan
mantenimiento y apoyar la toma de decisiones sobre
reparaciones o reemplazo de equipos.
"""
)

# 31. CONCLUSIONES

print("=" * 70)

print("CONCLUSIONES")

print("=" * 70)


print(
    """
1. Las redes neuronales pueden utilizarse para clasificar
el estado de los equipos de cómputo utilizando diferentes
variables de funcionamiento.

2. Variables como la temperatura del CPU, los errores del
sistema y el tiempo de arranque pueden proporcionar
información relevante sobre las condiciones de un equipo.

3. La separación entre datos de entrenamiento y prueba
permite evaluar el comportamiento del modelo con datos
que no fueron utilizados durante su aprendizaje.

4. La validación cruzada proporciona una evaluación más
confiable del modelo debido a que realiza diferentes
combinaciones de entrenamiento y prueba.

5. La matriz de confusión permite analizar con mayor
detalle los aciertos y errores realizados por la red
neuronal.

6. Si las métricas obtenidas permanecen altas durante la
validación cruzada, se puede considerar que el modelo
tiene una buena capacidad para generalizar.

7. El modelo podría utilizarse como una herramienta de
apoyo para detectar equipos que requieren mantenimiento
preventivo o correctivo.
"""
)


print("\nPROCESO TERMINADO CORRECTAMENTE.")