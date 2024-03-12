import numpy as np
import pandas as pd

tips = pd.read_csv("C:/Users/inoti/OneDrive/Documents/Python for ML and Data Science/03-Pandas/tips.csv")
print(tips.head(10))

print(tips.info())

print(str(123546789654)[-5:])

#Create a function that gives the last 4 digits of a string
def last_four(num):
    return str(num) [-4:]

#prints the whole Column CC Numbers last 4 digits
print(tips['CC Number'].apply(last_four))
#Adding a column named Last_four to the DataFRame
tips['last_four'] = tips['CC Number'].apply(last_four)
print(tips.head())

print(tips['total_bill'].mean())

#Creating a Function that checks the total_bill and assigns a $ depending on cost
def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else:
        return '$$$'
#Making a table for the $ called Yelp
tips['yelp'] = tips['total_bill'].apply(yelp)
print(tips)