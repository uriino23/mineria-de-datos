modelo.fit(X_train_escalado, y_train)

predicciones = modelo.predict(X_test_escalado)

exactitud = accuracy_score(y_test, predicciones)

print("\nExactitud del modelo:")
print(exactitud)

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, predicciones))

print("\nReporte de clasificación:")
print(classification_report(y_test, predicciones))

comparacion = pd.DataFrame({
    "Real": y_test.values,
    "Predicción": predicciones
})

print("\nComparación de resultados:")
print(comparacion)

nuevos_clientes = pd.DataFrame({
    "Compras_Mensuales": [1, 10, 18],
    "Gasto_Mensual_MXN": [500, 12000, 25000],
    "Visitas_Web_Mensuales": [2, 25, 50],
    "Satisfaccion": [2.5, 4.2, 5.0]
})

nuevos_clientes_escalados = escalador.transform(nuevos_clientes)

predicciones_nuevas = modelo.predict(nuevos_clientes_escalados)

print("\nPredicciones para nuevos clientes:")
print(predicciones_nuevas)
print("INTERPRETACION: La red neuronal identifica el nivel de consumo usando las compras, el gasto, las visitas web y la satisfacción. En general, los clientes con valores más altos en estas variables son clasificados como de alto consumo, mientras que los de valores bajos son clasificados como de bajo consumo.")
plt.plot(modelo.loss_curve_)
plt.xlabel("Iteraciones")
plt.ylabel("Error o pérdida")
plt.title("Proceso de aprendizaje de la red neuronal")
plt.show()

print("""¿Qué predicción obtuvo cada cliente?
Cliente 1: Bajo consumo.
Cliente 2: Alto consumo.
Cliente 3: Alto consumo.

¿La predicción tiene sentido?
Sí, porque los clientes con mayor gasto y más compras fueron clasificados con mayor consumo.

¿Qué variable parece influir más?
El gasto mensual, seguido del número de compras.

¿Qué pasa si aumentas el gasto mensual?
Es más probable que el cliente sea clasificado como de alto consumo.

¿Qué pasa si disminuyes la satisfacción?
Disminuye la probabilidad de que sea clasificado como de alto consumo.""")