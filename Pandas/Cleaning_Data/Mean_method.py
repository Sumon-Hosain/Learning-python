import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\book.csv')
x=var["Calories"].mean()        #Mean = the average value (the sum of all values divided by number of values).
var['Calories'].fillna(x,inplace= True)
print(var)