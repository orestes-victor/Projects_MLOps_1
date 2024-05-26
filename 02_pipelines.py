import pandas as pd
import numpy as np



def remove_negative_values(df, column):
    df[column] = df[column].apply(lambda x: np.nan if x < 0 else x)
    return df

def remove_ouliers_with_zscore(df, column, threshold = 2):
    column_mean =  df[column].mean()
    column_std = df[column].std()
    df[column] = df[column].mask(((df[column] - column_mean) / column_std).abs() > threshold, column_mean)
    return df 

def map_column_values(df, column, mapping_dict):
    df[column] = df[column].apply(lambda value: mapping_dict.get(value.lower().strip(), np.nan) if value is not np.nan else np.nan)
    return df

def fill_na_in_column(df, column, fill_value):
    df[column].fillna(fill_value, inplace=True)
    return df

def preprocess_data(df):

    education_mapping = {
        "Bachelors": "Bachelor",
        "mastre": "Master",
        "pHd": "PhD",
        "no education": "None"
    }

    gender_mapping = {
        "m" : "M",
        "f" : "F"
    }

    return (
        df.pipe(remove_negative_values, "Edad")
        .pipe(remove_negative_values, "Ingresos")
        .pipe(remove_negative_values, "Hijos")
        .pipe(remove_ouliers_with_zscore, "Edad")
        .pipe(remove_ouliers_with_zscore, "Ingresos")
        .pipe(remove_ouliers_with_zscore, "Altura")
        .pipe(remove_ouliers_with_zscore, "Hijos")
        .pipe(map_column_values, "Nivel_Educación", education_mapping)
        .pipe(map_column_values, "Género", gender_mapping)
        .pipe(fill_na_in_column, "Ciudad", "Desconocido")
        .pipe(fill_na_in_column, "Nivel_Educación", "Desconocido")
        .pipe(fill_na_in_column, "Género", "Desconocido")
        .pipe(fill_na_in_column, "Edad", df["Edad"].median())
        .pipe(fill_na_in_column, "Hijos", df["Hijos"].median())
        .pipe(fill_na_in_column, "Ingresos", df["Ingresos"].mean())
        .pipe(fill_na_in_column, "Edad", df["Edad"].mean())
    )


df = pd.DataFrame("tratamiento_datos.csv", index_col=0)
print(df)

df = preprocess_data(df)
print(df)
