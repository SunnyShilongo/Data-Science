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