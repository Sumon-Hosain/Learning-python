import pandas as pd
pd.options.display.max_rows=170
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data.csv')
var.fillna('10000',inplace=True)
print(var)
