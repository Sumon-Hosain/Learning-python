import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\book.csv')
x=var['Calories'].mean()           #Mean method avarages the coloumns value
var.fillna(x,inplace=True)      
print(var)