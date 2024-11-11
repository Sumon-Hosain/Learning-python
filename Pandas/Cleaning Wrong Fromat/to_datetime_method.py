import pandas as pd
var=pd.read_csv('E:\\Machine Learning Document\\Csv and Other documents\\3.csv')
var["Date"]=pd.to_datetime(var["Date"])
print(var)