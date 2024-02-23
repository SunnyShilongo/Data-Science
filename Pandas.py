import numpy as np
import pandas as pd

myindex = ['USA', 'Canada', 'Mexico']
mydata = [1776, 1867, 1821]

myser = pd.Series(data=mydata,index=myindex)
print(myser)

print(myser[0])
print(myser['USA'])
print(myindex[0])

ages = {'Sam':5, 'Frank':10, 'Spike':7}

pd.Series(ages)
print(pd.Series(ages))


''''Named Indexes'''
#Imaginary Sales Data for 1st and 2nd Quarters for Global Company
q1 = {'Japan': 80, 'China': 450, 'India': 220, 'USA': 250}
q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

print(q2) #Prints a dictionary
print(sales_q2) #Prints a Series

#When a certain name isn't in both Series Tables, a NAN (Not A Number) is inputted at the  location
print(sales_q2 + sales_q1)
print('This is not desired as it does not give much information on the data being reported on.')

#Using the .add method to bypass NAN being returned, but having it FILL_VALUE of 0 where the data is not in both Series Table
print(sales_q1.add(sales_q2, fill_value=0))