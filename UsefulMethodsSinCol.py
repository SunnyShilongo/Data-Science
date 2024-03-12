import numpy as np
import pandas as pd

tips = pd.read_csv("C:/Users/inoti/OneDrive/Documents/Python for ML and Data Science/03-Pandas/tips.csv")
print(tips.head(10))

print(tips.info())

print(str(123546789654)[-5:])


def last_four(num):
    return str(num) [-4:]

print(last_four(123456))