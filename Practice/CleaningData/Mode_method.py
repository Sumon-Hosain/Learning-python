import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\book.csv')
x=var['Calories'].mode()[0]           # Replace the empty value with most frequent value
var.fillna(x,inplace=True)
print(var)