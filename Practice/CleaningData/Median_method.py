import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\book.csv')
x=var['Calories'].median()    # median method replace the empty value with millde value of file
var.fillna(x,inplace=True)
print(var)