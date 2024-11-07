import pandas as pd
pd.options.display.max_rows=170
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data.csv')
var.dropna(inplace=True)           #'inplace=True' for changing the orginal document with null values
print(var)