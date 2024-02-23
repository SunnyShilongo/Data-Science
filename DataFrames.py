import numpy as np
import pandas as pd



''''DATAFRAMES

A DataFrame (DF) is a group of pandas Series object that SHARE the same index'''

np.random.seed(101)
mydata = np.random.randint(0,101,(4,3))
print(mydata)

myindex = ['CA','NY','AZ','TX']
mycolumns = ['Jan', 'Feb', 'Mar']

df = pd.DataFrame(data = mydata, index=myindex, columns=mycolumns) #Typical DF will have index and columns
print(df)
print(df.info())

# Two options to read in data / seperating the folders or \\
tips = pd.read_csv("C:/Users/inoti/OneDrive/Documents/Python for ML and Data Science/03-Pandas/tips.csv")
tips1 = pd.read_csv("C:\\Users\\inoti\\OneDrive\\Documents\\Python for ML and Data Science\\03-Pandas\\tips.csv")
print(tips1)
print(tips)

print(tips.head())
print(tips1.tail())

print('This in Column')
print(tips.columns) #Gives a list of the columns in the DF
print('This in index')
print(tips.index)# GIves the start and the Stop as well as the skze

print('This in info')
print(tips.info()) # INFORMATION ON DF
print('This in describe')
print(tips.describe()) # Gives statistical information on DATA in DF. Only does this on the numeric columns, bills but not name column