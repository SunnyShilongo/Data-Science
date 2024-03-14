import numpy as np
import pandas as pd

df = tips = pd.read_csv("C:/Users/inoti/OneDrive/Documents/Python for ML and Data Science/03-Pandas/tips.csv")
print(df)

print(df.describe().transpose())

#Sort Column, sorting defualt is always lowest to highest (ascending=True), for descending order (ascending=False)
print(df.sort_values('tip'))

#Sorting based on more than one column
print(df.sort_values(['tip', 'size']))
