import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\data.csv')
var1=var.head(100)
var1.fillna(10000,inplace=True)
print(var1.to_string())