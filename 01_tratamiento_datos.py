import pandas as pd  # Importa la biblioteca pandas para la manipulación de datos
import numpy as np  # Importa la biblioteca numpy para operaciones numéricas (aunque no se usa en este código)

# Lee el archivo CSV y lo carga en un DataFrame de pandas, utilizando la primera columna como índice
df = pd.read_csv("tratamiento_datos.csv", index_col=0)

# Imprime todo el DataFrame
#print(df)

# Imprime estadísticas descriptivas para las columnas numéricas del DataFrame
#print(df.describe())

# Muestra un resumen del DataFrame, incluyendo el número de entradas no nulas, tipos de datos de cada columna y uso de memoria
#print(df.info())

# Crea un conjunto único de valores en la columna "Género"
set_gen = set(df["Género"].to_list())

# Crea un conjunto único de valores en la columna "Nivel_Educación"
set_edu = set(df["Nivel_Educación"].to_list())

# Crea un conjunto único de valores en la columna "Ciudad"
set_ciu = set(df["Ciudad"].to_list())

# Imprime los conjuntos únicos de valores para "Género", "Nivel_Educación" y "Ciudad"
#print(set_gen)
#print(set_edu)
#print(set_ciu)


# 1. Tratamiento de valores negativos
# Si el valor en la columna "Edad" es negativo, se reemplaza por NaN; de lo contrario, se deja el valor original.
df["Edad"] = df["Edad"].apply(lambda x: np.nan if x < 0 else x)

# Si el valor en la columna "Ingresos" es negativo, se reemplaza por NaN; de lo contrario, se deja el valor original.
df["Ingresos"] = df["Ingresos"].apply(lambda x: np.nan if x < 0 else x)

# Si el valor en la columna "Hijos" es negativo, se reemplaza por NaN; de lo contrario, se deja el valor original.
df["Hijos"] = df["Hijos"].apply(lambda x: np.nan if x < 0 else x)

# 2. Imputar valores faltantes
# Para cada columna en ["Edad", "Ingresos", "Hijos"], se calcula la mediana y se rellenan los valores faltantes con la mediana.
for column in ["Edad", "Ingresos", "Hijos"]:
    median_value = df[column].median()
    df[column].fillna(median_value, inplace=True)

# Para cada columna en ["Género", "Ciudad"], se calcula la moda y se rellenan los valores faltantes con la moda.
for column in ["Género", "Ciudad"]:
    mode_value = df[column].mode()[0]
    df[column].fillna(mode_value, inplace=True)

# 3. Mapeo de datos
# Se define un diccionario para mapear los valores de la columna "Nivel_Educación" a nuevos valores.
education_mapping = {
    "Bachelors": "Bachelor",
    "mastre": "Master",
    "pHd": "PhD",
    "no education": "None"
}

# Se reemplazan los valores en la columna "Nivel_Educación" utilizando el diccionario definido.
df["Nivel_Educación"].replace(education_mapping, inplace=True)
df["Nivel_Educación"].fillna("NE",inplace=True)

# Casteo de tipos (nos aseguramos que cada columna tenga su tipo correcto)

df["Edad"] = df["Edad"].astype(int)
df["Hijos"] = df["Hijos"].astype(int)
df["Ingresos"] = df["Ingresos"].astype(float)
df["Altura"] = df["Altura"].astype(float)

# Imprime todo el DataFrame
print(df)

# Imprime estadísticas descriptivas para las columnas numéricas del DataFrame
print(df.describe())

# Muestra un resumen del DataFrame, incluyendo el número de entradas no nulas, tipos de datos de cada columna y uso de memoria
print(df.info())

