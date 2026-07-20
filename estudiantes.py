import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


df = pd.read_csv("estudiantes_modelo(1).csv")

X = df[["Asistencia", "Tareas", "Examen", "Horas_Estudio"]]
y = df["Resultado"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

exactitud = accuracy_score(y_test, predicciones)

print("Predicciones:")
print(predicciones)

print("Resultados reales:")
print(y_test.values)

print("Exactitud del modelo:")
print(exactitud)

print("Matriz de confusión:")
print(confusion_matrix(y_test, predicciones))

#print("Reporte de clasificación:")
#print(classification_report(y_test, predicciones))

nuevos_estudiantes = pd.DataFrame({
    "Asistencia": [95, 60, 78],
    "Tareas": [90, 55, 80],
    "Examen": [92, 50, 70],
    "Horas_Estudio": [12, 3, 7]
})

nuevas_predicciones = modelo.predict(nuevos_estudiantes)

print(nuevas_predicciones)