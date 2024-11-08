import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\2.csv')
var['Date']=pd.to_datetime(var["Date"])
print(var.to_string())