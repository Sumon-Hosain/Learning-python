import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\4.csv')
var.drop_duplicates(inplace=True)
print(var)