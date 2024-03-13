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

''''LAMBDA EXPRESSIONS
What is a lambda expression?
It is good for once off expression you don't plan on using a lot'''

def simple(num):
    return num * 2
#For lambda change teh def to

print(simple(2))

lambda num: num*2


print(tips['total_bill'].apply(lambda num: num*2))



def quality(total_bill, tip):
    if tip / total_bill > 0.25:
        return "Generous"
    else:
        return "Other"

print(quality(16.99,1.01))
#Select columns "tips[['total_bill', 'tip']]"
#Call Lambda on the dataFrame being passed in "lambda tips"
#Into the function we pass in the columns
print(tips[['total_bill', 'tip']].apply(lambda tips: quality(tips['total_bill'],tips['tip']), axis=1))

#assign thos to column
#tips['Quality'] = tips[['total_bill', 'tip']].apply(lambda tips: quality(tips['total_bill'],tips['tip']), axis=1)
print(tips)

tips['Quality'] = np.vectorize(quality)(tips['total_bill'], tips['tip'])
print(tips)



