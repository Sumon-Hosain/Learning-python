import pandas as pd
pd.options.display.max_rows=170
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\book.csv')
var['Calories'].fillna(10000,inplace=True)       #Replacing columns's data  with specific value
print(var)