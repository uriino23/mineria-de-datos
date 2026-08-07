import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("dataset_clientes-1.csv")

X = df[[
    "Compras_Mensuales",
    "Gasto_Mensual_MXN",
    "Dias_Desde_Ultima_Compra"
]]

X = X.dropna()

escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)

modelo = KMeans(n_clusters=3, random_state=42, n_init=10)

clusters = modelo.fit_predict(X_escalado)

df_limpio = X.copy()
df_limpio["Cluster"] = clusters

print(df_limpio)

print("\nPromedio por clúster:")
print(df_limpio.groupby("Cluster").mean())

inercias = []

max_k = min(7, len(X_escalado))

for k in range(1, max_k + 1):
    modelo = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    modelo.fit(X_escalado)
    inercias.append(modelo.inertia_)

plt.plot(range(1, max_k + 1), inercias, marker="o")
plt.xlabel("Número de clusters K")
plt.ylabel("Inercia")
plt.title("Método del codo")
plt.show()

#Interpretacion
print("Interpretacion: El algoritmo K-Means agrupó a los clientes en tres clústeres con características similares, considerando las variables compras mensuales, gasto mensual y días desde la última compra. Los resultados muestran que cada grupo presenta un comportamiento de compra diferente, lo que permite identificar segmentos de clientes para diseñar estrategias específicas de marketing, promociones y fidelización; el numero de clousters utilizados en esta prueba fue de tres en una temporada de mensual, el clouster 0 nos muestra a los clientes poco frecuentes, mientras que el clouster 1 nos refleja a los clientes constantes y finalmente el clouster 2 se muestra a los clientes regulares. Con estos resultados podemos aprovecharlos para ver con que clientes podemos agregar mayor atencion o algun sevivio para aumentar su consumo. mientras que en la grafica se visualiza la brecha de tiempo entre una compra y otra. ")