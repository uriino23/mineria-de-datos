import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score

# 1. Cargar y limpiar datos
df = pd.read_csv('dataset_sucursales_mensual.csv')

# Imputar nulos con la mediana para evitar perder registros
cols_with_nans = ['Gasto_Publicidad', 'Descuento_Promedio', 'Satisfaccion_Cliente', 'Devoluciones']
for col in cols_with_nans:
    df[col] = df[col].fillna(df[col].median())

# 2. Métodos estadísticos (Tendencia central y dispersión)
stats_cols = ['Clientes_Atendidos', 'Gasto_Publicidad', 'Descuento_Promedio', 'Satisfaccion_Cliente', 'Ventas_Totales']
stats_df = df[stats_cols].describe().T[['mean', '50%', 'std', 'min', 'max']]
stats_df.columns = ['Media', 'Mediana (50%)', 'Desv. Estándar', 'Mínimo', 'Máximo']
# Moda para cada una
modas = df[stats_cols].mode().iloc[0]
stats_df['Moda'] = modas

print("MEDIDAS DE TENDENCIA CENTRAL Y DISPERSIÓN")
print(stats_df.to_string())
print("\n")

# 3. Correlaciones
print("ANÁLISIS DE CORRELACIONES CON VENTAS TOTALES")
corr_publicidad = df['Gasto_Publicidad'].corr(df['Ventas_Totales'])
corr_clientes = df['Clientes_Atendidos'].corr(df['Ventas_Totales'])
corr_satisfaccion = df['Satisfaccion_Cliente'].corr(df['Ventas_Totales'])
corr_descuento = df['Descuento_Promedio'].corr(df['Ventas_Totales'])

print(f"Correlación entre Publicidad y Ventas: {corr_publicidad:.4f}")
print(f"Correlación entre Clientes atendidos y Ventas: {corr_clientes:.4f}")
print(f"Correlación entre Satisfacción y Ventas: {corr_satisfaccion:.4f}")
print(f"Correlación entre Descuento y Ventas: {corr_descuento:.4f}")
print("\n")

# 4. Clasificación: Predecir Cumplio_Meta
# Variables predictoras (X) y objetivo (y)
X_class_cols = ['Clientes_Atendidos', 'Gasto_Publicidad', 'Descuento_Promedio', 'Satisfaccion_Cliente', 'Ventas_Totales']
X_class = df[X_class_cols]
# Normalizar target: "Si"/"No" -> 1/0
le = LabelEncoder()
y_class = le.fit_transform(df['Cumplio_Meta'].str.strip().str.lower().replace({'sí': 'si'})) # Asegurar consistencia

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_class, y_class, test_size=0.25, random_state=42)

# Árbol de Decisión
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train_c, y_train_c)
y_pred_dt = dt.predict(X_test_c)

# Naive Bayes
nb = GaussianNB()
nb.fit(X_train_c, y_train_c)
y_pred_nb = nb.predict(X_test_c)

# Regresión Logística (requiere escalado)
scaler = StandardScaler()
X_train_c_scaled = scaler.fit_transform(X_train_c)
X_test_c_scaled = scaler.transform(X_test_c)

lr = LogisticRegression(random_state=42)
lr.fit(X_train_c_scaled, y_train_c)
y_pred_lr = lr.predict(X_test_c_scaled)

print("MODELOS DE CLASIFICACIÓN (Cumplio_Meta)")
print(f"Exactitud (Accuracy) - Árbol de Decisión: {accuracy_score(y_test_c, y_pred_dt):.4f}")
print(f"Exactitud (Accuracy) - Naive Bayes: {accuracy_score(y_test_c, y_pred_nb):.4f}")
print(f"Exactitud (Accuracy) - Regresión Logística: {accuracy_score(y_test_c, y_pred_lr):.4f}")
print("\n")

# 5. Regresión: Predecir Ventas_Totales
# Regresión lineal simple (ej. Clientes Atendidos vs Ventas Totales)
X_simple = df[['Clientes_Atendidos']]
y_reg = df['Ventas_Totales']
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_simple, y_reg, test_size=0.25, random_state=42)

reg_simple = LinearRegression()
reg_simple.fit(X_train_s, y_train_s)
y_pred_s = reg_simple.predict(X_test_s)

# Regresión lineal múltiple (múltiples variables predictoras)
X_mult = df[['Clientes_Atendidos', 'Gasto_Publicidad', 'Descuento_Promedio', 'Satisfaccion_Cliente']]
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_mult, y_reg, test_size=0.25, random_state=42)

reg_mult = LinearRegression()
reg_mult.fit(X_train_m, y_train_m)
y_pred_m = reg_mult.predict(X_test_m)

print("MODELOS DE REGRESIÓN (Predecir Ventas_Totales)")
print("Regresión Lineal Simple (Predictor: Clientes_Atendidos):")
print(f"  R2 Score: {r2_score(y_test_s, y_pred_s):.4f}")
print(f"  RMSE: {np.sqrt(mean_squared_error(y_test_s, y_pred_s)):.2f}")
print("Regresión Lineal Múltiple (Predictores: Clientes, Publicidad, Descuento, Satisfacción):")
print(f"  R2 Score: {r2_score(y_test_m, y_pred_m):.4f}")
print(f"  RMSE: {np.sqrt(mean_squared_error(y_test_m, y_pred_m)):.2f}")