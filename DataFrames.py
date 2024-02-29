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

print(tips.head())


''''Columns'''
#Calling one column is just the DataFrame name plus the column in square brackets
print(tips['total_bill'])

#Calling multiple columns at once. Remember the double square brackets
print(tips[['total_bill', 'tip', 'Payer Name']])

#Arthemic calculation can be done on Columns by calling the DataFrame and the columns to be used
#e.g. Total Percentage of the tip to the total bill
print(100 * tips['tip'] / tips['total_bill'])

#Adding a new column, reference the new column as an preexsisting column and it will be add to the end
#NB If you make a new column and the Column name already exists, the data in the existing column will be overwritten
tips['Tip and Bill'] = tips['total_bill'] + tips['tip']
#OR
tips['Tip_Percentage'] = 100 * tips['tip'] / tips['total_bill']
print(tips.head())

#Rounding by 2 decimal places. Use numpy np.round, then calculation and add the number of decimals at the end
tips['Tip and Bill'] = np.round(tips['total_bill'] + tips['tip'],2)
tips['Tip_Percentage'] = np.round(100 * tips['tip'] / tips['total_bill'],3)
print(tips.head())

#Dropping a column is done with .drop() DO NOT forget axis. 0 is Row, 1 is column
#NB Remember it is possible that you drop a column but didn't make it permenant to the column
print(tips.drop('Tip and Bill', axis = 1)) # Not Permenant
tips = tips.drop('Tip and Bill', axis = 1) # Permenant
print(tips)

'''ROWS'''
#Changing Index(Unique Identifier/Primary Key)
#print(df.index())
print(tips.index)
print(tips.set_index("Payment ID"))

#Make it Permanent
tips = tips.set_index('Payment ID')

print(tips.head)

#Reset the Index
tips = tips.reset_index()
print(tips.head)