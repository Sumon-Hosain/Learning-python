import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\book.csv')
x=var['Calories'].mode()[0]       #Mode = the value that appears most frequently.
var.fillna(x,inplace=True)
print(var)