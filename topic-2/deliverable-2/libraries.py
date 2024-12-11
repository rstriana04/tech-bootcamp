#Uso de pandas
# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt


# Cargar el dataset Iris desde una URL funcional
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)


# Revisar las primeras filas para verificar las columnas
#print(df.head())


# Crear un gráfico de dispersión entre "sepal_length" y "sepal_width"
df.plot(x="sepal_length", y="sepal_width", kind="scatter", title="Scatter Plot of Sepal Dimensions")


# Mostrar el gráfico
plt.show()


# Crear un gráfico de barras para la cantidad promedio de sepal_width por especie
df.groupby("species")["sepal_width"].mean().plot(kind="bar", title="Average Sepal Width by Species", color="skyblue")


# Etiquetas del gráfico
plt.xlabel("Species")
plt.ylabel("Average Sepal Width")


# Mostrar el gráfico
plt.show()


# Revisar las primeras filas para verificar las columnas
print(df.head())


# Contar el número de ocurrencias por especie
species_counts = df["species"].value_counts()


# Crear un gráfico de torta
species_counts.plot(
    kind="pie",
    autopct="%1.1f%%",  # Mostrar porcentajes
    startangle=90,      # Rotar inicio a 90 grados
    title="Distribution of Species"
)


# Asegurar que el gráfico sea circular
plt.axis("equal")


# Mostrar el gráfico
plt.show()


#Uso de numpy y matplotlib
#Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Crear un DataFrame con datos ficticios
data = {
    "Edad": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    "Creditos": [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500],
}
df = pd.DataFrame(data)  # Crear el DataFrame a partir del diccionario de datos


# Calcular la media de la columna "Creditos"
mean_balance = df["Creditos"].mean()  # Almacenar la media en una variable


# Agregar una columna que indique si la edad es mayor de 40
df["es_mayor_de_40"] = df["Edad"] > 40  # Crear una nueva columna con valores booleanos


# Filtrar el DataFrame para obtener solo las filas donde la edad es mayor de 40
df_mayores_40 = df[df["Edad"] > 40]  # Crear un nuevo DataFrame filtrado


# Calcular la suma acumulativa de la columna "Creditos"
df["suma_acumulativa_Creditos"] = df["Creditos"].cumsum()  # Sumar los créditos acumulativamente


# Graficar la relación entre "Edad" y "Creditos"
# Gráfico de líneas
plt.plot(df["Edad"], df["Creditos"], marker='o', linestyle='--', color='b')  # Usar círculos como marcadores
plt.title("Tendencia de Créditos por Edad")  # Título del gráfico
plt.xlabel("Edad")  # Etiqueta del eje X
plt.ylabel("Créditos")  # Etiqueta del eje Y
plt.grid()  # Agregar una cuadrícula para mejor visualización
plt.show()  # Mostrar el gráfico


# Gráfico de barras
plt.bar(df["Edad"], df["Creditos"], color='orange')  # Usar barras de color naranja
plt.title("Créditos por Edad")  # Título del gráfico
plt.xlabel("Edad")  # Etiqueta del eje X
plt.ylabel("Créditos")  # Etiqueta del eje Y
plt.xticks(df["Edad"])  # Asegurar que las edades se muestren en el eje X
plt.show()  # Mostrar el gráfico



#Cargar Datos
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Cargar dataset de ejemplo
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print(data.head())
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data.drop('species', axis=1)) # Normalizando los datos




# Matplotlib
import matplotlib.pyplot as plt # Importa la librería Matplotlib para visualización de gráficos
categorias = ['A', 'B', 'C', 'D'] # Nombres de las categorías en el eje X
valores = [23, 45, 56, 78] # Valores correspondientes a cada categoría en el eje Y
plt.figure(figsize=(8, 6)) # Define el tamaño del gráfico (ancho, alto)
plt.bar(categorias, valores, color='blue') # Dibuja las barras, cada barra representando una categoría
# Añadir un título al gráfico
plt.title('Gráfico de barras con Matplotlib') #Establece el título del gráfico
plt.xlabel('Categorías') # Etiqueta para el eje X
plt.ylabel('Valores') # Etiqueta para el eje Y
plt.show() # Muestra el gráfico en la pantalla





#Seaborn
import seaborn as sns # Importa la librería Seaborn, que está basada en Matplotlib para gráficos más estilizados
import matplotlib.pyplot as plt # También se importa Matplotlib para usar la función plt.show()
categorias = ['A', 'B', 'C', 'D'] # Nombres de las categorías en el eje X
valores = [23, 45, 56, 78] # Valores correspondientes a cada categoría en el eje Y
sns.set(style="whitegrid") # Configura un estilo de cuadrícula de fondo para que los gráficos se vean más limpios
plt.figure(figsize=(8, 6)) # Define el tamaño del gráfico (ancho, alto)
sns.barplot(x=categorias, y=valores,
            palette="Blues_d") # Dibuja las barras, usando una paleta de colores azul degradado
plt.title('Gráfico de barras con Seaborn') # Establece el título del gráfico
plt.show() # Muestra el gráfico en la pantalla



