import numpy as np
import pandas as pd

df = tips = pd.read_csv("C:/Users/inoti/OneDrive/Documents/Python for ML and Data Science/03-Pandas/tips.csv")
print(df)

#Shows Analyzes both numeric and object series, as well as DataFrame column sets of mixed data types.
#The output will vary depending on what is provided
print(df.describe().transpose())

''''SORTING'''
#Sort Column, sorting defualt is always lowest to highest (ascending=True), for descending order (ascending=False)
print(df.sort_values('tip'))

#Sorting based on more than one column
print(df.sort_values(['tip', 'size']))

''''
.max - Used to get the highest value in the DataFrame
.idxmax - Used to get the index location of the highest value in the DataFrame'''
# .max gives the highest value in the column ['column name']. Think max = Maximum
print(df['total_bill'].max())
# .idxmax give the index location of the max value
print(df['total_bill'].idxmax())
# Get the information of the item at index value []
print(df.iloc[170])

''''
.min - Used to get the lowest value in the DataFrame
.idxmin - Used to get the index location of the lowest value in the DataFrame'''
# .min gives the lowest value in the column ['column name']. Think min = Minimum
print(df['total_bill'].min())
# .idxmin give the index location of the min value
print(df['total_bill'].idxmin())
# Get the information of the item at index value []
print(df.iloc[67])

#Simplify without knowning the index value
#asking for the information, based on the lowest value in the column, then state the lowest value
print(df.iloc[df['total_bill'].idxmin()])
print('New Line')
print(df.iloc[df['total_bill'].idxmin()])

#How Correlated are the values
print(df.corr())

#Value Counts - Gives a count of the different values in the column
print(df['sex'].value_counts())

''''
UNIQUE - Used to find all the values that are unique
NUNIQUE - Used to give the Number of Unique Values found in the DataFrame'''
#Unique - Returns the unique days in the dataset
print(df['day'].unique())
#nunique - Gives the number of unique values
print(df['day'].nunique())
#Get the number of values for the different instances
print(df['day'].value_counts())

''''REPLACE METHOD
Best for repalcing fewer items'''
#This can handle multiple values at once as shown below
print(df['sex'].replace(['Female', 'Male'], ['F', 'M']))
#This is for handling a single value
print(df['sex'].replace('Female', 'F'))

''''MAP METHOD
This is best for working with a lot of items'''
#Create a dictionary of the values and the key
MyGender = {'Female':'F','Male':'M'}
#map based on the dictionary created
print(df['sex'].map(MyGender))

'''DUPLICATE
Run against the dataframe. 
It would return True anytime there is an instance of a duplicate in the DF
False means there is no Duplicates in the DataFrame'''
print(df.duplicated())

''''DROPPING DUPLICATES
If there are any duplicates they would get dropped. 
Only the first instance is kept all duplicates that follow get removed'''
print(df.drop_duplicates())

'''Between 
Allows for selection based on values between certain values
inclusive allows for the selection of values that are 100% on the dot of the upper and lower limit'''
print(df['total_bill'].between(10,20,inclusive=True))

#Using Conditional Filters to print only the rows that match the wanted output
print(df[df['total_bill'].between(10,20,inclusive=True)])

'''NLARGEST - Gives the rows that had the largest n from a column
df.nlargest( n= number of values wanted, ['column to look in'])'''
print(df.nlargest(10,'tip'))
print(df.nlargest(10,['tip']))

'''NSMALLEST - Gives the rows that had the smallest n from a column
df.nsmallest( n= number of values wanted, ['column to look in'])'''
print(df.nsmallest(10,'tip'))
print(df.nsmallest(10,['tip']))

''''SMAPLING - Used for getting random samples from the DF
Can also use frac = ABC to get a percentage of the entire DF. value should be less then (>) 1'''
print(df.sample(5))
print(df.sample(frac=0.2))