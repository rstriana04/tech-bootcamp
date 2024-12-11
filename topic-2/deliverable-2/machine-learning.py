import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar datos
data = pd.DataFrame({
    'Estudiante': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Sofía', 'Carlos', 'Elena', 'Jorge', 'Lucía'],
    'Horas_de_estudio': [5, 10, 7, 12, 4, 9, 6, 8, 11, 3],
    'Participación_clase': [7, 9, 8, 10, 6, 9, 7, 8, 10, 5],
    'Nota_final': [70, 85, 78, 92, 65, 88, 74, 80, 90, 60]
})
print("Datos iniciales:")
print(data)

# 2. Preprocesar (limpiar y normalizar)
X = data[['Horas_de_estudio', 'Participación_clase']] # Variables predictoras
y = data['Nota_final'] # Variable objetivo

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) # Normalización

print("\nDatos normalizados:")
print(X_scaled)

# 3. Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 4. Entrenar un modelo
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluar y ajustar el modelo
print(f"\nPrecisión del modelo (R^2): {model.score(X_test, y_test):.2f}")

# Visualización de predicciones vs valores reales
predictions = model.predict(X_test)
plt.scatter(y_test, predictions)
plt.xlabel('Valores Reales (Nota Final)')
plt.ylabel('Predicciones (Nota Final)')
plt.title('Predicciones vs Valores Reales')
plt.show()

# Visualización adicional
sns.pairplot(data[['Horas_de_estudio', 'Participación_clase', 'Nota_final']])
plt.show()

sns.heatmap(data[['Horas_de_estudio', 'Participación_clase', 'Nota_final']].corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de correlación')
plt.show()