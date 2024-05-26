import pandas as pd
import numpy as np

df = pd.DataFrame("tratamiento_datos.csv", index_col=0)

def remove_negative_values(df, column):
    df[column] = df[column].apply(lambda x: np.nan if x < 0 else x)
    return df

def remove_ouliers_with_zscore(df, column, threshold = 2):
    column_mean =  df[column].mean()
    column_std = df[column].std()
    df[column] = df[column].mask(((df[column] - column_mean) / column_std).abs() > threshold, column_mean)
    return df 

def map_column_values(df, column, mapping_dict):
    df[column] = df[column].apply(lambda value: mapping_dict.get(value.lower()))