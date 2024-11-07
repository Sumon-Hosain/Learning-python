import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\book.csv')
x=var['Calories'].median() #Median = the value in the middle, after you have sorted all values ascending.
var.fillna(x,inplace=True)
print(var)