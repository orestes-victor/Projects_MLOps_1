import pandas as pd 
import numpy as np 

df =  pd.read_csv("tratamiento_datos.csv", index_col=0)

print(df)
print(df.describe())
print(df.info())

set_gen = set(df["Género"].to_list())
set_edu = set(df["Nivel_Educación"].to_list())
set_ciu = set(df["Ciudad"].to_list())

print(set_gen)
print(set_edu)
print(set_ciu)